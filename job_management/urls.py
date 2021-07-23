
from .views import *
from django.urls import path


app_name = 'jobmanage'

urlpatterns = [
    path('create_job/', create_job, name='create-job'),
    path('job_det/<int:job_id>', job_det, name='job-det'),
    path('apply_job/<int:job_id>/', apply_job, name='apply-job'),
    path('manage_jobs/', manage_jobs, name='manage-jobs'),
    path('update_post/<int:job_id>/', update_post, name='update-post'),
    path('manage_applic/', manage_applic, name='manage-applic'),
    path('status_change/', status_change, name='status-change'),
    path('companydetails/', companydetails, name='company-details'),
    path('short_listed/', short_listed),
]
