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
    current_salary = models.IntegerField(blank=True,null=True)
    currency = models.CharField(max_length=25,blank=True,null=True)
    photo = models.ImageField(upload_to='applicants/profile_pictures',blank=True, null=True)
    resume = models.FileField(upload_to='applicants/documents',blank=True)
    contact_no = models.CharField(max_length=30,null=True)
    description = models.TextField()

    class Meta:
        verbose_name_plural  = "Seekers' profile"

    def __str__(self):
        return self.user.first_name

    def save(self, *args, **kwargs):
        if not self.contact_no:
            self.contact_no = self.user.contact_no
        super().save(*args, **kwargs)

    @property
    def get_photo_url(self):
        if self.photo is not None:
            return f"{self.photo.url}"
        else:
            return " "

    @property
    def get_resume_url(self):
        try:
            return f"{self.resume.url}"
        except ValueError:
            return "/"


class ExperienceDetail(models.Model):
    profile = models.ForeignKey(SeekerProfile, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    job_title = models.CharField(max_length=20)
    company_name = models.CharField(max_length=200)
    job_location_state = models.CharField(max_length=50)
    job_location_city = models.CharField(max_length=50)
    job_location_country = models.CharField(max_length=60)
    total_years = models.PositiveIntegerField(null=True,blank=True)
    description = models.TextField()

    class Meta:
        verbose_name_plural  = "Seekers' experience details"


class EducationDetail(models.Model):
    profile = models.ForeignKey(SeekerProfile, on_delete=models.CASCADE)
    certificate_degree_name = models.CharField(max_length=255)
    major = models.CharField(max_length=255)
    institute_university_name = models.CharField(max_length=255)
    starting_date = models.DateField()
    completion_date = models.DateField()

    class Meta:
        verbose_name_plural  = "Seekers' education details"


class Seekerskillset(models.Model):
    skill_name = models.CharField(max_length=24,null=True)
    seeker = models.ForeignKey(SeekerProfile, on_delete=models.CASCADE)
    skill_level = models.CharField(max_length=25)

    class Meta:
        verbose_name = 'Seeker skill set'
        verbose_name_plural  = "Seeker's skills"


    def __str__(self):
        return f"{self.skill_name}"

    # @property
    # def get_seekers_skills(self):
    #     return self.skillset_set.all()
