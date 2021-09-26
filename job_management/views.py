

from django.contrib import messages
from django.utils import tree
from companyprofile.models import CompanyImage
from django.http.response import JsonResponse
from seekerbuilder.models import SeekerProfile
from companyprofile.models import Company
from job_management.models import *
from django.shortcuts import get_object_or_404, redirect, render
from django.core.exceptions import *
from seekerbuilder.models import Seekerskillset
from django.db.models import Q
# Create your views here.
import schedule

from schedule import every, repeat


def create_job(request):
    company_ = Company.objects.values_list('name', flat=True)
    # job_skill = Skillset.objects.all()
    # job_skill_set = Job_Skillset.get_skill_level.display()

    if request.method == 'POST':
        job_title = request.POST['job_title']
        company_name = request.POST['company_name']
        company = get_object_or_404(Company, name__iexact=company_name)
        address = request.POST.get('street_addr')
        city = request.POST['city']
        state = request.POST['state']
        country = request.POST['country']
        zip_ = request.POST.get('zip_code')
        skill_names = request.POST.getlist('skill_name')
        start_salary = request.POST.get('salary_start')
        end_salary = request.POST.get('salary_end')

        # create job skills if not already present inside DB
        print(skill_names)
        skill_list = []
        for skill in skill_names:
            skill_nam, created = Skillset.objects.get_or_create(skill_name__iexact=skill,defaults={
                'skill_name' : skill
            })
            skill_list.append(skill)
        
        job_descrip = request.POST['job_descrip']
        job_skill_ = request.POST.getlist('job_skill_level')
        job_pst = JobPost.objects.create(title=job_title, 
                          cmpny_name=company, job_description=job_descrip, salary_start=start_salary,salary_end=end_salary)
        job_pst.job_posters.add(request.user)
        job_pst.save()

        job_loc = JobLocation(job=job_pst,address=address, city=city,
                              state=state, country=country, zip_code=zip_)
        job_loc.save()

        #skill_list has skill names job level has skill level required
        job_skill_set = []
        for job_skill_name, job_level in zip(skill_list, job_skill_):
            job_skillset = Job_Skillset(skill_name=job_skill_name,job_post=job_pst, skill_level=job_level)
            job_skill_set.append(job_skillset)

        Job_Skillset.objects.bulk_create(job_skill_set)
        messages.add_message(request,messages.SUCCESS,'Job post successfully submitted!')
        return redirect('/dashboard/')

    return render(request, 'company/company_entry.html', context={
        'contxt': 'job_contxt',
        'company': company_,
        # 'skills_req': job_skill,

    })


# getting details of specific jobs


def job_det(request, job_id):
    # fetching specific job detail

    job_det = JobPost.objects.get(id=job_id)
    applied = False
    if request.user.is_authenticated:
        try:
            applied_user = JobPostActivity.objects.get(
                user=request.user, job_post__id=job_id)
            print(applied_user)
            applied = True

        except(ObjectDoesNotExist):
            applied = False
    return render(request, 'company/company_details.html', context={
        'job_det': job_det,
        'applied': applied
    })


def companydetails(request):
    if request.method == 'GET':
        filter_ = request.GET.get('id')
        print(filter_)
        cmpny = Company.objects.get(id=filter_)
        cmpny_images = CompanyImage.objects.filter(company__id=filter_)
        context = {
            'cmpny': cmpny,
            'cmpny_images': cmpny_images[0]
        }
    return render(request, 'company/company_details.html', context)

# data fetching when user clicks apply now


def apply_job(request, job_id):
    if request.method == 'GET':
        try:
            seeker_profile = SeekerProfile.objects.get(user=request.user)
            job = JobPost.objects.get(id=job_id)

            applied_job, created = JobPostActivity.objects.get_or_create(
                user=request.user, job_post__id=job_id, defaults={
                    'user': request.user,
                    'job_post': job
                })
            messages.add_message(request,messages.SUCCESS,f'your application has been sent to {job.cmpny_name}')
        except ObjectDoesNotExist:
            if SeekerProfile.DoesNotExist:
                messages.add_message(request,messages.INFO,'Kindly add the profile first')
        print(request.META['HTTP_REFERER'])
        return redirect('/dashboard/')


def manage_jobs(request):
    jobs_created = JobPost.objects.filter(job_posters=request.user)
    if request.GET.get('job'):
        job_id = request.GET.get('job')
        JobPost.objects.filter(id = job_id).delete()
    return render(request, 'jobmanagment/job_details.html', context={
        'jobs_created': jobs_created,
        'user': 'HR',
    })


def update_post(request, job_id):

    job_post = JobPost.objects.get(id=job_id)
    print('jobpost',job_post)
    try:
        job_location = JobLocation.objects.get(job = job_post)
    except ObjectDoesNotExist:
        job_location = JobLocation()
        print('no address found')
    if request.method == 'POST':
        job_post.job_title = request.POST.get('title')
        company_name = request.POST.get('company_name')
        compny = get_object_or_404(Company, name__iexact=company_name)
        address = request.POST.get('street_addr')
        city = request.POST['city']
        state = request.POST['state']
        country = request.POST['country']
        zip_code = request.POST['zip_code']
        job_post.salary_start = request.POST.get('salary_start')
        job_post.salary_end = request.POST['salary_end']
        job_post.job_descrip = request.POST['job_descrip']
        job_post.job_posters.add(request.user)
        job_post.cmpny_name = compny
        job_post.save()

        job_location.jobpost = job_post
        job_location.address =address
        job_location.city = city
        job_location.state = state
        job_location.country = country
        job_location.zip_code = zip_code
        job_location.save()

        
        messages.add_message(request,messages.SUCCESS,'job details updated! ')
        return redirect('/dashboard/')

    company_ = Company.objects.values_list('name', flat=True)
    return render(request, 'company/company_entry.html', context={
        'company': company_,
        'contxt': 'job_contxt',
        'val': job_post,
        'update': True,
        'address' : job_location
    })

# shortlisting candidates
# ----------------------------


def manage_applic(request):
    if request.method == 'GET':
        # getting onhold candidates
        applied_candi = JobPostActivity.objects.filter(
            job_post__job_posters=request.user).exclude(Q(status__iexact='rejected') | Q(status__iexact='selected'))
        context = {
            'manage_applic': True,
            'applicants': applied_candi,

        }
        return render(request, 'jobmanagment/applicants_manage.html', context)


# Change user job req status using ajax
def status_change(request):
    if request.method == 'GET':

        status = request.GET.get('selected_val')
        filter_ = request.GET.get('id')
        title = request.GET.get('job_title')
        prof = JobPostActivity.objects.get(
            user__id=int(filter_), job_post__title=title)
        prof.status = status
        prof.save()
        return JsonResponse(status=200, data={
            'selected_status': status
        })


def short_listed(request):
    if request.method == 'GET':
        selected_candid = JobPostActivity.objects.filter(
            job_post__job_posters=request.user).exclude(Q(status__iexact='rejected') | Q(status__iexact='onhold'))
        context = {
            'selected_candid': selected_candid
        }
        return render(request, 'jobmanagment/applicants_manage.html', context)




def saved_jobs(request):
    if request.method == 'GET':
        if request.GET.get('user'):
            user = request.GET.get('user')
            print(user)
            saved_jobs = SavedJobs.objects.filter(user__username = user)
        else:
            user = saved_jobs = None
            messages.add_message(request,messages.INFO,"No saved jobs")
        
        context = {
            'saved_job' : saved_jobs
        }
        return render(request,"manageusers/saved_jobs.html",context)