
from .models import SeekerProfile, ExperienceDetail, EducationDetail
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from manageusers.models import User
from django.core.exceptions import *
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.core.cache import cache
from job_management.models import Skillset
# Create your views here.
from seekerbuilder.models import *

# for application form


@csrf_exempt
def update_details(request):
    seeker = get_object_or_404(User, id=request.user.id)
    if request.method == "POST":

        # seeker profile insertion if there is no data present else update
        try:
            user = SeekerProfile.objects.get(user=request.user)
        except (ObjectDoesNotExist):
            print('from exception')
            user = SeekerProfile()
        user.user = seeker
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.current_salary = request.POST['current_salary']
        user.currency = request.POST['currency']
        user.save()
        skill_name = request.POST.getlist('skill_name')
        skill_level = request.POST.getlist('skill_level')
        # print(f'skill name-> {skill_name} skill level ->{skill_level}')
        seeker_skll = []


        # testing destructing
        for skill_nme, skill_lvl in zip(skill_name, skill_level):
            skill_set = Skillset.objects.get(skill_name=skill_nme)
            seeker_skll.append(Seekerskillset(
                skill_set=skill_set, skill_level=skill_lvl, seeker=user))
            print(seeker_skll)
      

        seeker_bulk = Seekerskillset.objects.bulk_create(seeker_skll)
        print('after insertion',seeker_bulk)
        return redirect('/users/dashboard')

    skill_names = Skillset.objects.all()
    return render(request, 'manageusers/application_form.html', context={
        'applicant': seeker,
        'type': 'updatedetail',
        'skill_names': skill_names
    })


# For updating education details
def update_edu(request):
    seeker = get_object_or_404(SeekerProfile, user=request.user)
    user, created = EducationDetail.objects.get_or_create(profile=seeker, defaults={
        'starting_date': datetime.datetime.now(),
        'completion_date': datetime.datetime.now(),
    })
    if request.method == 'POST':
        # try:
        #     user = EducationDetail.objects.get(profile=seeker)
        # except(ObjectDoesNotExist):
        #     user = EducationDetail()
        user.profile = seeker
        user.certificate_degree_name = request.POST['degree_name']
        user.major = request.POST['major']
        user.institute_university_name = request.POST['ins_university_name']
        user.starting_date = request.POST['starting_date']
        user.completion_date = request.POST['completion_date']
        user.save()

        return redirect('/users/dashboard/')

    return render(request, 'manageusers/application_form.html', context={
        'type': 'updateeducation',
        'applicant': user,
    })


def update_exper(request):
    seeker = get_object_or_404(SeekerProfile, user=request.user)
    user, created = ExperienceDetail.objects.get_or_create(profile=seeker, defaults={
        'start_date': datetime.datetime.now(),
        'end_date': datetime.datetime.now(),
    })
    if request.method == 'POST':
        # try:
        #     user = EducationDetail.objects.get(profile=seeker)
        # except(ObjectDoesNotExist):
        #     user = EducationDetail()
        user.profile = seeker
        user.start_date = request.POST['start_date']
        user.end_date = request.POST['end_date']
        user.job_title = request.POST['job_title']
        user.company_name = request.POST['company_name']
        user.job_location_state = request.POST['job_location_state']
        user.job_location_city = request.POST['job_location_city']
        user.job_location_country = request.POST.get('job_location_country')
        user.description = request.POST.get('description')
        user.save()
        return redirect('/users//dashboard/')

    return render(request, 'manageusers/application_form.html', context={
        'type': 'updateexper',
        'applicant': user,
    })

    # for updating experience
