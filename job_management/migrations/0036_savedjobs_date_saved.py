# Generated by Django 3.2.5 on 2021-09-25 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_management', '0035_jobpost_requirement_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='savedjobs',
            name='date_saved',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]