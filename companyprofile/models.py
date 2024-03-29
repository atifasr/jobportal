from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import tree

# Create your models here.




# creating company model depening on business streams
class Company(models.Model):
    
    name = models.CharField(max_length=255)
    prof_description = models.TextField(null=True,blank=True)
    estab_date = models.DateTimeField(null=True)
    company_website = models.URLField(max_length=255,null=True)
    contact_email = models.EmailField(blank=False,null=True)

    class Meta:
        verbose_name = 'Company'

    def __str__(self):
        return str(self.name)




class BuisnessStream(models.Model):
    buisness_stream_name = models.CharField(max_length=255)
    company = models.ManyToManyField(Company)

    class Meta:
        verbose_name = 'BuisnessStream'

    def __str__(self):
        return self.buisness_stream_name


class CompanyImage(models.Model):
    cover_image = models.ImageField(upload_to='images/company_cover')
    images = models.ImageField(upload_to='images')
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'CompanyImage'
