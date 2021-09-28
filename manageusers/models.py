from datetime import date, time
import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.db import models

# Create your models here.


# from typing_extensions import Required
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.db.models.base import ModelState
from django.db.models.deletion import CASCADE
from django.db.models.expressions import Case
from django.db.models.fields.related import ForeignKey
from django.forms import widgets
from companyprofile.models import Company


from django.conf import settings
# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not username:
            raise ValueError('Users must have an email address')

        user = self.model(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email='', password=None):
        user = self.create_user(first_name='', last_name='',
                                username=username, email=email, password=password)
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user




class User(AbstractBaseUser):
    USER_TYPE = [('HR', 'Recuriter'), ('job_seeker', 'Job_seeker')]
    JOB_SEEKER = 'job_seeker'
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(default='1995-03-25')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    company = models.ForeignKey(Company,on_delete=models.CASCADE,null=True,blank=True)
    user_type = models.CharField(max_length=255, choices=USER_TYPE,default=JOB_SEEKER)
    gender = models.CharField(max_length=22,blank=True,null=True)
    contact_no = models.CharField(max_length=30, null=True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,

    )

    

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    @property
    def get_message_count(self):
        try:
            messages_count = Messages.objects.filter(message_thread__receiver = self,opened=False).count()
        except ObjectDoesNotExist:
            messages_count = 0
        return messages_count

    def save(self, *args, **kwargs):
        if self.email:
            self.username = self.email.split('@')[0]
        super().save(*args, **kwargs)






class Address(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    city = models.CharField(max_length=10)
    state = models.CharField(max_length=12,blank=True)
    zip_code = models.CharField(max_length=12,blank=True)
    street = models.CharField(max_length=255,blank=True)



# User's last login and apply date information
class UserLog(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    last_login_date = models.DateTimeField()
    last_job_apply_date = models.DateField(auto_now=True)




class MessageThreads(models.Model):
    sender = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name='sender', null=True)
    receiver = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name='receiver', null=True)
    created_date = models.DateField(auto_now_add=True)
    created_time = models.TimeField(auto_now_add=True)


    



class Messages(models.Model):
    message_thread = models.ForeignKey(MessageThreads,on_delete=models.CASCADE,null=True)
    message = models.TextField(max_length=600,blank=True)
    sent_date = models.DateField(auto_now_add=True)
    sent_time = models.TimeField(auto_now_add=True)
    opened = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.message[:10]}"



