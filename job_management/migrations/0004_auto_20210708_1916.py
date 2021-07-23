# Generated by Django 3.2.4 on 2021-07-08 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_management', '0003_jobpost_jobpostactivity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobtag',
            name='job_type',
        ),
        migrations.AddField(
            model_name='jobtag',
            name='job_type',
            field=models.ManyToManyField(to='job_management.JobType'),
        ),
    ]
