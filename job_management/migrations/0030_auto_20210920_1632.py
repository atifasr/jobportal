# Generated by Django 3.2.5 on 2021-09-20 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_management', '0029_jobcategories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobcategories',
            name='jobpost',
        ),
        migrations.AddField(
            model_name='jobcategories',
            name='jobpost',
            field=models.ManyToManyField(to='job_management.JobPost'),
        ),
    ]
