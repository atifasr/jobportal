from .views import *
from django.urls import path


app_name = 'manageusers'

urlpatterns = [
    path('', home, name='home-page'),
    path('reg/', user_reg, name='user-reg'),
    path('login/', login_, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('application_form/', app_form, name='app-form'),
    path('log_out/', log_out, name='log-out'),
    path('get_jobs/', get_jobs, name='get-jobs'),
    path('get_jobs_ajax/', get_jobs_ajax, name='get_job_aj'),
    path('search_func/', search_func),
    path('profile_view/<int:job_id>/', profile_view, name='profile_view'),
]
