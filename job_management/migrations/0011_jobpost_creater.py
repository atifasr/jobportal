# Generated by Django 3.2.4 on 2021-07-10 15:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('job_management', '0010_alter_jobpostactivity_apply_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='creater',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='manageusers.user'),
            preserve_default=False,
        ),
    ]
