from companyprofile.models import Company
from django.db import models
from django.db.models.base import Model, ModelState
from manageusers.models import User
from django.conf import settings

# Create your models here.

# model for a Job post
class JobPost(models.Model):
    job_posters = models.ManyToManyField(
        settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=255)
    
    # Company job post belongs to
    cmpny_name = models.ForeignKey(
        Company, related_name='company', on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    job_description = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.job_type)

    @property
    def get_jobposters(self):
        return f'{self.job_posters.all()}'



# locations for a particular post
class JobLocation(models.Model):
    address = models.TextField()
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    country = models.CharField(max_length=25)
    zip_code = models.CharField(max_length=25)
    job = models.ForeignKey(JobPost, on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.city


class JobType(models.Model):
    job_type = models.CharField(max_length=255)
    job = models.ForeignKey(
        JobPost, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return str(self.job_type)

# for popular tags
class JobTag(models.Model):
    name = models.CharField(max_length=255)
    job = models.ManyToManyField(JobPost)


# when users appies for a job
class JobPostActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job_post = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    apply_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=25, default='onhold')

    def __str__(self):
        return self.user.username+''+self.job_post.title


level = [('beginner', 'BEGINNNER'), ('intermediate',
                                     'INTERMEDIATE'), ('expert', 'EXPERT')]


class Skillset(models.Model):
    skill_name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.skill_name)


class Job_Skillset(models.Model):
    job_post = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    skill = models.ForeignKey(
        Skillset, on_delete=models.CASCADE)
    skill_level = models.CharField(max_length=20)
