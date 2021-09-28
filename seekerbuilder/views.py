
import json
from job_management.models import Job_Skillset
from manageusers.models import Address
from django.contrib import messages
from .models import SeekerProfile, ExperienceDetail, EducationDetail
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from manageusers.models import User
from django.core.exceptions import *
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.core.cache import cache
from job_management.models import Skillset,JobPost,SavedJobs
# Create your views here.
from seekerbuilder.models import *
from django.http.response import JsonResponse

# for application form

# creating or updating user details
@csrf_exempt
def update_details(request):
    try:
        prof = SeekerProfile.objects.get(user= request.user)
    except SeekerProfile.DoesNotExist:
        prof = None
    if request.method == "POST":
        curr_user = User.objects.get(id= request.user.id)
        # seeker profile insertion if there is no data present else update
        try:
            user = SeekerProfile.objects.get(user=request.user)
        except (ObjectDoesNotExist):
            print('from exception')
            user = SeekerProfile()

        # updating users profile
        curr_user.first_name = request.POST['first_name']
        curr_user.last_name = request.POST['last_name']
        curr_user.contact_no = request.POST.get('contact_no')
        curr_user.description = request.POST.get('description')
        curr_user.date_of_birth = request.POST.get('date_of_birth')
        curr_user.gender = request.POST.get('gender')
        curr_user.save()


        # updating Seekers profile
        user.user = curr_user
        user.first_name = curr_user.first_name
        user.last_name = curr_user.last_name
        user.resume = request.FILES.get('resume')
        print(request.FILES.get('photo'))
        user.photo = request.FILES.get('photo')

        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')
        address_street = request.POST.getlist('address_street')


        try:
            user_address = Address.objects.filter(user = curr_user)
            for index,address in enumerate(address_street):
                user_address[index].street = address
                user_address[index].city = city
                user_address[index].zip_code = zip_code
                user_address[index].state = state
                user_address[index].save()
        except Address.DoesNotExist:
            address_obj_list = []
            for value in address_street:
                address_obj_list.append(Address(
                    user = curr_user,
                    street = value,
                    city= city,
                    state = state,
                    zip_code =zip_code
                )
                )
            Address.objects.bulk_create(address_obj_list)

        user.save()

        messages.add_message(request,messages.INFO,'Details updated'.capitalize())
        return redirect('/dashboard/')

    skill_names = Skillset.objects.all()
    return render(request, 'manageusers/application_form.html', context={
        'type': 'updatedetail',
        'skill_names': skill_names,
        'prof':prof    
    })


# For updating education details
def update_edu(request):
    try:
        seeker = SeekerProfile.objects.get(user=request.user)
        edu_ins, created = EducationDetail.objects.get_or_create(profile=seeker, defaults={
            'starting_date': datetime.datetime.now(),
            'completion_date': datetime.datetime.now(),
        })
        seeker_skills = Seekerskillset.objects.filter(seeker = seeker)
        print(seeker_skills)
    except SeekerProfile.DoesNotExist:
        seeker = SeekerProfile()
        seeker_skills = Seekerskillset()

    if request.method == 'POST':
        certificate_degree_name = request.POST['degree_name']
        major = request.POST['major']
        institute_university_name = request.POST['ins_university_name']
        starting_date = request.POST['starting_date']
        completion_date = request.POST['completion_date']
        
        edu_ins.profile = seeker
        edu_ins.certificate_degree_name = certificate_degree_name
        edu_ins.major = major
        edu_ins.institute_university_name = institute_university_name
        edu_ins.starting_date = starting_date
        edu_ins.completion_date = completion_date
        edu_ins.save()        

        return redirect('/dashboard/')

    return render(request, 'manageusers/application_form.html', context={
        'type': 'updateeducation',
        'applicant': edu_ins,
        'seeker_skills':seeker_skills
    })


def update_exper(request):
    try:
        seeker = SeekerProfile.objects.get(user=request.user)
        user, created = ExperienceDetail.objects.get_or_create(profile=seeker, defaults={
            'start_date': datetime.datetime.now(),
            'end_date': datetime.datetime.now(),
        })
    except ObjectDoesNotExist:
        user = None
       
    if request.method == 'POST':
        user.profile = seeker
        user.start_date = request.POST.get('starting_date')
        user.end_date = request.POST.get('completion_date')
        user.job_title = request.POST['job_title']
        user.company_name = request.POST['company_name']
        user.description = request.POST.get('description')
        user.save()
        return redirect('/dashboard/')

    return render(request, 'manageusers/application_form.html', context={
        'type': 'updateexper',
        'applicant': user,
    })

    # for updating experience



#saving Jobs
def save_job(request):
    if request.method == 'GET':
        job_id = request.GET.get('id')
        user_job  = request.GET.get('us_job')
        saved_status ={
            'saved':False
        }
        job_ins = JobPost.objects.get(id = job_id)
        user_ins = User.objects.get(username = user_job)
        job_created_ins,created = SavedJobs.objects.get_or_create(user = user_ins,job=job_ins)
        if not created:
            saved_status['saved'] = True
        else:
            saved_status['saved'] = False
        return JsonResponse(saved_status,safe='False')




@csrf_exempt
def delete_skill(request):
    if request.method == 'POST':
        data = {}
        
        job_id = request.body.decode('utf-8')
        job_id = json.loads(job_id)
        job_id = int(job_id['skill_id'])
        try:
            Seekerskillset.objects.get(id=job_id).delete()
            data['status'] = 'deleted'
        except ObjectDoesNotExist:
            data['status'] = 'nodata'
        return JsonResponse(data,safe=False)



@csrf_exempt
def add_skill(request):
    if request.method == "POST":
        seeker_skills = request.body.decode('utf-8')
        seeker_skills = json.loads(seeker_skills)
        job_skill_list = []
        seeker_prof = SeekerProfile.objects.get(user=request.user)
        for skill_ins in seeker_skills:
            job_skill_list.append(
                Seekerskillset(
                    seeker = seeker_prof,
                    skill_name = skill_ins['skill_name'],
                    skill_level = skill_ins['skill_level']
                )
            )
        Seekerskillset.objects.bulk_create(job_skill_list)

        resp ={
            'status':'updated'
        }
        return JsonResponse(resp,safe=False)
