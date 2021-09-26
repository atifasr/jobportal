from .views import *
from django.urls import path


app_name = 'seekerbuilder'
urlpatterns = [
    path('app_det/', update_details, name='app-det'),
    path('update_exper/', update_exper, name='update-exper'),
    path('update_edu/', update_edu, name='update-edu'),
    path('save_job/',save_job,name = "save-job"),
    path('delete_skill/',delete_skill,name = "delete_skill"),
    path('add_skill/',add_skill,name = "add-skill"),

]
