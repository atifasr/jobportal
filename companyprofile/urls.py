from django.urls import path
from .views import *

app_name = 'company'

urlpatterns = [

    path('comp_create/', create_comp, name='create-comp'),


]
