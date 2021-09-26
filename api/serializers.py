from job_management.models import JobPostActivity
from companyprofile.models import Company
from job_management import models
from django.db.models import fields
from job_management.models import JobPost, JobLocation
from rest_framework import serializers
from job_management import *
from manageusers.models import User


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class JoblocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobLocation
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    job_loc = JoblocationSerializer(source='joblocation_set',many= True)
    cmpny_name = CompanySerializer()

    class Meta:
        model = JobPost
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class JobactivitySerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = JobPostActivity
        fields = '__all__'
