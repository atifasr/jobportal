

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
    job_skill = Skillset.objects.all()
    # job_skill_set = Job_Skillset.get_skill_level.display()

    if request.method == 'POST':
        # getting company by name for reference

        job_title = request.POST['job_title']
        company_name = request.POST['company_name']
        compny = get_object_or_404(Company, name__iexact=company_name)
        address = request.POST.get('address')
        city = request.POST['city']
        state = request.POST['state']
        country = request.POST['country']
        zip_ = request.POST['zip']
        jobtype = request.POST['job_type']
        salary = request.POST['salary']
        tag = request.POST.get('job_tag')

        # creating jobtype entered by user
        job_type, created = JobType.objects.get_or_create(job_type=jobtype)
        job_tag, creatd = JobTag.objects.get_or_create(name=tag)

        job_loc = JobLocation(address=address, city=city,
                              state=state, country=country, zip=zip_)
        job_loc.save()

        job_descrip = request.POST['job_descrip']

        job_skill_ = request.POST.getlist('job_skill_name[]')
        job_skill_level = request.POST.getlist('job_skill_level[]')
        job_pst = JobPost(creater=request.user, title=job_title, job_type=job_type, job_loc=job_loc,
                          cmpny_name=compny, job_description=job_descrip, salary=salary)

        job_pst.save()

        job_skill_set = []
        for job_skll, job_lvl in zip(job_skill_, job_skill_level):
            skil_set = Skillset.objects.get(skill_name=job_skll)
            job_skill_set.append(Job_Skillset(
                skill=skil_set, job_post=job_pst, skill_level=job_lvl))

        Job_Skillset.objects.bulk_create(job_skill_set)

        return redirect('/users/dashboard')
    return render(request, 'company/company_entry.html', context={
        'contxt': 'job_contxt',
        'company': company_,
        'skills_req': job_skill,

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
        job = JobPost.objects.get(id=job_id)
        applied_job, created = JobPostActivity.objects.get_or_create(
            user=request.user, job_post__id=job_id, defaults={
                'user': request.user,
                'job_post': job
            })

        return redirect('/users/dashboard')


def manage_jobs(request):
    jobs_created = JobPost.objects.filter(creater=request.user)
    return render(request, 'jobmanagment/job_details.html', context={
        'jobs_created': jobs_created,
        'user': 'HR',
    })


def update_post(request, job_id):
    job_post = JobPost.objects.get(id=job_id)
    if request.method == 'POST':
        job_post.job_title = request.POST.get('title')
        company_name = request.POST['company_name']
        compny = get_object_or_404(Company, name__iexact=company_name)
        address = request.POST.get('address')
        city = request.POST['city']
        state = request.POST['state']
        country = request.POST['country']
        zip_ = request.POST['zip']
        jobtype = request.POST['job_type']
        job_post.salary = request.POST['salary']
        tag = request.POST.get('job_tag')
        job_post.job_descrip = request.POST['job_descrip']

        job_type, created = JobType.objects.get_or_create(job_type=jobtype)
        job_tag, creatd = JobTag.objects.get_or_create(name=tag)
        # job_loc = JobLocation(address)

        job_loc = JobLocation(address=address, city=city,
                              state=state, country=country, zip=zip)
        job_loc.save()
        job_post.creater = request.user
        job_post.job_loc = job_loc
        job_post.job_type = job_type
        job_post.cmpny_name = compny
        job_post.save()

        return redirect('/users/dashboard')

    company_ = Company.objects.values_list('name', flat=True)
    return render(request, 'company/company_entry.html', context={
        'company': company_,
        'contxt': 'job_contxt',
        'val': job_post,
        'update': True
    })

# shortlisting candidates
# ----------------------------


def manage_applic(request):
    if request.method == 'GET':
        # getting onhold candidates
        applied_candi = JobPostActivity.objects.filter(
            job_post__creater=request.user).exclude(Q(status__iexact='rejected') | Q(status__iexact='selected'))
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
            'message': 'okay'
        })


def short_listed(request):
    selected_candid = JobPostActivity.objects.filter(
        job_post__creater=request.user).exclude(Q(status__iexact='rejected') | Q(status__iexact='onhold'))
    print('working')
    context = {
        'selected_candid': selected_candid
    }
    return render(request, 'jobmanagment/applicants_manage.html', context)
