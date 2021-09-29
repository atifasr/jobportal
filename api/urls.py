from django.urls import path
from .views import *

urlpatterns = [

    path('get_applicants/', get_applic),
    path('dashboard_data/', dashboard_data),

]
