from copy import error
import json
from typing import ContextManager
from django.db.models.query_utils import Q

from pytz import timezone

from seekerbuilder.models import SeekerProfile, ExperienceDetail, Seekerskillset
from job_management.models import JobPostActivity
from django.http.response import Http404, HttpResponse, JsonResponse
from django.shortcuts import redirect, render, resolve_url

from django.http import request
from .models import Messages, User, UserLog ,Address,MessageThreads
from companyprofile.models import Company
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from datetime import date, datetime
from django.core.exceptions import ObjectDoesNotExist
from job_management.models import JobPost
from django.core.cache import cache
from rest_framework.decorators import api_view, permission_classes
from api.serializers import *
from django.core.paginator import Paginator
from django.contrib import messages

# ---------------------------------imports

def number_cmpy():
    try:
        no_of_compy = Company.objects.all()
    except(ObjectDoesNotExist):
        return None
    return no_of_compy.count()


# displaying all the companies and jobs

@api_view(['GET'])
def get_jobs_ajax(request):
    if request.method == 'GET':

        jobs = JobPost.objects.all()
        serialized = PostSerializer(jobs, many=True)
        return JsonResponse(serialized.data, safe=False)

from .helpers import push_data
def home(request):

    if request.method == 'GET':
        objects = JobPost.objects.all().order_by('-created_date')
        
        p = Paginator(objects, 14)
        if request.GET.get('page_num'):
            page_num = request.GET.get('page_num')
            jobs = p.page(page_num).object_list

        else:
            jobs = p.page(1).object_list 
            
        return render(request, 'manageusers/home.html', context={
            'jobs': jobs,
            'page': p,
        })


# def get_page():
#     if request.method == 'GET':
#         jobs = JobPost.objects.all()
#         p = Paginator(jobs, 6)
#         pag_no = request.GET.get('page_num')
#         print(p.num_pages)
#         return render(request, 'manageusers/home.html', context={
#             'jobs': p.page(pag_no).object_list,
#             'page': p,
#         })


@csrf_exempt
def user_reg(request):
    if request.method == 'POST':
        gender = request.POST.get('gender')
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        date_of_birth = request.POST.get('date_of_birth')
        contact_no = request.POST['contact_no']
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')

        user = User(
            gender=gender, 
            email=email, 
            first_name=first_name,
            last_name=last_name, 
            date_of_birth=date_of_birth, 
            contact_no=contact_no,
            user_type=user_type
            )
        user.set_password(password)
        user.save()

        city = request.POST.getlist('city')
        state = request.POST.getlist('state')
        zip_code = request.POST.getlist('zip_code')
        address_street = request.POST.getlist('address_street')
        
        address_obj_list = []
        for index,value in enumerate(address_street):

            address_obj_list.append(Address(
                user = user,
                street = value,
                city= city[index],
                state = state[index],
                zip_code =zip_code[index]
            )
            )
        Address.objects.bulk_create(address_obj_list)
        
        return redirect('/login/')
    return render(request, 'manageusers/user_registration.html')


@csrf_exempt
def login_(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username, password=password)
            if user is not None:
                login(request, user=user)
                log = UserLog(user=user, last_login_date=datetime.now())
                log.save()
                return redirect('/')
            else:
                messages.add_message(request,messages.WARNING,'Check username or password!')
                return redirect('/login/')
    return render(request, 'manageusers/login.html', {
        'title': 'login'
    })

# for logging out users
def log_out(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            logout(request)
        return redirect('/login/')
       


# Hr or Seeker Dashboard

def dashboard(request):
    if request.method == "GET":
        no_of_comp = number_cmpy()
        if request.user.user_type == 'HR':
            try:
                created_posts = JobPost.objects.filter(job_posters=request.user)
                companies = Company.objects.all()
            except ObjectDoesNotExist:
                print(' no data ')

            applicants = JobPostActivity.objects.filter(
                job_post__job_posters=request.user)
            recent_ones = applicants.order_by('-apply_date')[:3]
            context = {
                'created_posts': created_posts,
                'applicants': applicants,
                'recent_app': recent_ones,
                'companies': companies
            }
        else:
            try:
                seeker_profile = SeekerProfile.objects.get(user=request.user)
                applied_posts = JobPostActivity.objects.filter(user=request.user)
                recently_applied = applied_posts.order_by('-apply_date')[:5]

                seeker_skill = Seekerskillset.objects.filter(
                    seeker__user=request.user)
                edu_det = ExperienceDetail.objects.filter(
                    profile__user=request.user)
                print(applied_posts)
            except ObjectDoesNotExist:
                print('calling from here')

                if SeekerProfile.DoesNotExist:
                    seeker_profile = None

                if JobPostActivity.DoesNotExist:
                    recently_applied = applied_posts = None

                if Seekerskillset.DoesNotExist:
                    seeker_skill = None
                if ExperienceDetail.DoesNotExist:

                    edu_det = None

            context = {
                'seeker_profile': seeker_profile,
                'applied_posts': applied_posts,
                'recently_applied': recently_applied,
                'seeker_skill': seeker_skill,
                'edu_det': edu_det
            }
        return render(request, 'manageusers/dashboard.html', context)





def app_form(request):
    if request.method == 'GET':
        pass
    return render(request, 'manageusers/application_form.html')


# user search function for searching jobs
def search_func(request):
    if request.method == 'GET':
        filter_srch = request.GET.get('search_text')
        filter_type = request.GET.get('filter')
        context = {}
        if filter_type == 'title':
        #    search by title
            fltrd_obj = JobPost.objects.filter(
                title__icontains=filter_srch)

        elif filter_type == 'company_name':
            # search by company name
            fltrd_obj = JobPost.objects.filter(
                cmpny_name__name__icontains=filter_srch)
           
           
        else:
            fltrd_obj = JobPost.objects.filter(
                job_type__job_type__icontains=filter_srch)
            
        
        p = Paginator(fltrd_obj,18)
        if request.GET.get('page_num'):
            page_num = request.GET.get('page_num')
            jobs = p.page(page_num).object_list
        else:
            jobs = p.page(1).object_list 

        context['jobs'] = jobs
        messages.add_message(request,messages.INFO, f"{jobs.count()} Matching results")

        return render(request, 'manageusers/home.html', context)


# seekergetting jobs
def get_jobs(request):
    if request.method == 'GET':
        jobs_applied = JobPostActivity.objects.filter(user=request.user)
        context = {
            'jobs_applied': jobs_applied
        }
        return render(request, 'jobmanagment/job_details.html', context)



def profile_view(request,job_id):
    if request.method == 'GET':
        profile = SeekerProfile.objects.get(user__id=job_id)
        context = {
            'profile': profile
        }
        return render(request, 'manageusers/profile.html', context)



@csrf_exempt
def send_message(request):
    if request.method == 'POST':
        resp = {}
        resp_data = request.body.decode('utf-8')
        resp_data = json.loads(resp_data)
        receiver = User.objects.get(username = resp_data['receiver'])
        sender = User.objects.get(username = resp_data['sender'])
        message = resp_data['message']
        message_thread,created = MessageThreads.objects.get_or_create(
            sender = sender,
            receiver = receiver, defaults={
                'sender':sender,
                'receiver':receiver
            }  
        )

        Messages.objects.create(
            message_thread = message_thread,
            message =message
        )
        resp['status'] = 'sent'
        return JsonResponse(resp,safe=False)



def message_list(request):
    if request.method == "GET":
        message_threads = MessageThreads.objects.filter(Q(sender = request.user) | Q(receiver = request.user)).order_by('-created_date')
        print(message_threads)
        return render(request,'manageusers/messages.html',{
            'message_threads':message_threads
        })
