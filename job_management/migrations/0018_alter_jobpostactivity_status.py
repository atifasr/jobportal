# Generated by Django 3.2.5 on 2021-07-23 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_management', '0017_jobpostactivity_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobpostactivity',
            name='status',
            field=models.CharField(default='onhold', max_length=25),
        ),
    ]
