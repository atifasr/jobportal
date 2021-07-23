# Generated by Django 3.2.4 on 2021-07-07 14:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('companyprofile', '0003_auto_20210705_1357'),
        ('job_management', '0002_jobtag'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField()),
                ('job_description', models.CharField(max_length=255)),
                ('cmpny_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companyprofile.company')),
                ('job_loc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_management.joblocation')),
                ('job_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_management.jobtype')),
            ],
        ),
        migrations.CreateModel(
            name='JobPostActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apply_date', models.DateField()),
                ('job_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job_management.jobpost')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
