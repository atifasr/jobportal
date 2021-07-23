from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.


class BuisnessStream(models.Model):
    buisness_stream_name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'BuisnessStream'

    def __str__(self):
        return self.buisness_stream_name


# creating company model depening on business streams
class Company(models.Model):
    stream = models.ForeignKey(BuisnessStream, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    prof_description = models.TextField()
    estab_date = models.DateTimeField()
    company_website = models.URLField(max_length=255)

    class Meta:
        verbose_name = 'Company'

    def __str__(self):
        return str(self.name)


class CompanyImage(models.Model):
    cover_image = models.ImageField(upload_to='images/company_cover')
    images = models.ImageField(upload_to='images')
    company = models.ForeignKey(Company, on_delete=CASCADE)

    class Meta:
        verbose_name = 'CompanyImage'
