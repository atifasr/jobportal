from .views import *
from django.urls import path


app_name = 'seekerbuilder'
urlpatterns = [
    path('app_det/', update_details, name='app-det'),
    path('update_edu/', update_edu, name='update-edu'),
    path('update_exper/', update_exper, name='update-exper'),
]
