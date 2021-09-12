from typing import ContextManager

from seekerbuilder.models import SeekerProfile, ExperienceDetail, Seekerskillset
from job_management.models import JobPostActivity
from django.http.response import Http404, HttpResponse, JsonResponse
from django.shortcuts import redirect, render, resolve_url

from django.http import request
from .models import User, UserLog
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


def home(request):
    if request.method == 'GET':
        jobs = JobPost.objects.all()
        p = Paginator(jobs, 6)
        print(p)
        print(p.page(1).object_list)
        print(p.page(2).object_list)
        print(p.num_pages)
        # print(p.count)

        return render(request, 'manageusers/home.html', context={
            'jobs': p.page(1).object_list,
            'page': p,
        })


def get_page():
    if request.method == 'GET':
        jobs = JobPost.objects.all()
        p = Paginator(jobs, 6)
        pag_no = request.GET.get('page_num')
        print(p.num_pages)
    return render(request, 'manageusers/home.html', context={
        'jobs': p.page(pag_no).object_list,
        'page': p,
    })


@csrf_exempt
def user_reg(request):
    if request.method == 'POST':
        gender = request.POST.get('gender')
        print(gender)
        email = request.POST['email']
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        date_of_birth = request.POST['date_of_birth']
        contact_no = request.POST['contact_no']
        password = request.POST.get('password')

        user = User(gender=gender, email=email, username=username, first_name=first_name,
                    last_name=last_name, date_of_birth=date_of_birth, contact_no=contact_no)
        user.set_password(password)
        user.save()

        return redirect(reverse('manageusers:login'), permanent=True)

    user = User()
    return render(request, 'manageusers/user_registration.html', context={
        'user': user
    })


@csrf_exempt
def login_(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user=user)
            log = UserLog(user=user, last_login_date=datetime.now())
            log.save()
            print(log)
            return redirect('users/dashboard')
        else:
            return render(request, 'manageusers/login.html', {
                'title': 'login',
                'message': 'try again with correctpasscode'
            })
    return render(request, 'manageusers/login.html', {
        'title': 'login'
    })


def log_out(request):
    if request.method == 'GET':
        logout(request)
        return redirect('../login')


def dashboard(request):
    # using caching to store retrieved data objects
    if request.method == "GET":
        if cache.get('no_of_company'):
            print('Date already in cache')
            no_of_comp = cache.get('no_of_company')
            print(no_of_comp)
        else:
            cache.set('no_of_company', number_cmpy())
            no_of_comp = cache.get('no_of_company')
            print('Database accessed')
            print(no_of_comp)

        if request.user.user_type == 'HR':
            created_posts = JobPost.objects.filter(creater=request.user)
            companies = Company.objects.all()

            applicants = JobPostActivity.objects.filter(
                job_post__creater=request.user)
            recent_ones = applicants.order_by('-apply_date')[:3]
            print(recent_ones)
            context = {
                'created_posts': created_posts,
                'applicants': applicants,
                'recent_app': recent_ones,
                'companies': companies
            }
        else:
            seeker_profile = SeekerProfile.objects.get(user=request.user)
            applied_posts = JobPostActivity.objects.filter(user=request.user)
            recently_applied = applied_posts.order_by('-apply_date')[:5]

            seeker_skill = Seekerskillset.objects.filter(
                seeker__user=request.user)
            edu_det = ExperienceDetail.objects.filter(
                profile__user=request.user)

            # print(seeker_profile.photo.url)
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
        print(filter_type)
        context = {}

        if filter_type == 'title':
            print(f'filter is {filter_type}')
            fltrd_obj = JobPost.objects.filter(
                title__icontains=filter_srch)
            print(fltrd_obj)
            context['jobs'] = fltrd_obj
            messages.success(request, 'Matching results')
        elif filter_type == 'company_name':
            # cmpny_name
            fltrd_obj = JobPost.objects.filter(
                cmpny_name__name__icontains=filter_srch)
            print(fltrd_obj)
            print(f'filter is {filter_type}')
            context['jobs'] = fltrd_obj
            messages.success(request, 'Matching results')
        else:
            fltrd_obj = JobPost.objects.filter(
                job_type__job_type__icontains=filter_srch)
            print(fltrd_obj)
            print(f'filter is {filter_type}')
            context['jobs'] = fltrd_obj

            # messages.error(request, 'No Matching result.')
            # return redirect('/users')

        return render(request, 'manageusers/home.html', context)


# seekergetting jobs
def get_jobs(request):
    if request.method == 'GET':
        jobs_applied = JobPostActivity.objects.filter(user=request.user)
        context = {
            'jobs_applied': jobs_applied
        }
        return render(request, 'jobmanagment/job_details.html', context)


def get_profile(request):
    pass


def profile_view(request):
    if request.method == 'GET':
        id_ = request.GET.get('id')

        profile = SeekerProfile.objects.get(user__id=id_)
        context = {
            'profile': profile
        }
        return render(request, 'manageusers/profile.html', context)