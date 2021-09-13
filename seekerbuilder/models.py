from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.utils import tree
from manageusers.models import User
from companyprofile.models import Company
from job_management.models import Skillset
# Create your models here.


class SeekerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    current_salary = models.IntegerField()
    currency = models.CharField(max_length=25)
    photo = models.ImageField(upload_to='applicants',blank=True, null=True)
    resume = models.FileField(upload_to='applicants/documents')

    def __str__(self):
        return self.user.first_name


class ExperienceDetail(models.Model):
    profile = models.ForeignKey(SeekerProfile, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    job_title = models.CharField(max_length=20)
    company_name = models.CharField(max_length=200)
    job_location_state = models.CharField(max_length=50)
    job_location_city = models.CharField(max_length=50)
    job_location_country = models.CharField(max_length=60)
    description = models.TextField()


class EducationDetail(models.Model):
    profile = models.ForeignKey(SeekerProfile, on_delete=models.CASCADE)
    certificate_degree_name = models.CharField(max_length=255)
    major = models.CharField(max_length=255)
    institute_university_name = models.CharField(max_length=255)
    starting_date = models.DateField()
    completion_date = models.DateField()


class Seekerskillset(models.Model):
    skill_set = models.ForeignKey(Skillset, on_delete=models.CASCADE)
    seeker = models.ForeignKey(SeekerProfile, on_delete=models.CASCADE)
    skill_level = models.CharField(max_length=25)

    class Meta:
        verbose_name = 'Seeker skill set'


    def __str__(self):
        return f"{self.skill_set.skill_name} {self.skill_level}"