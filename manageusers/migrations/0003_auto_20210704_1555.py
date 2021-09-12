# Generated by Django 3.2.4 on 2021-07-04 10:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manageusers', '0002_auto_20210704_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='contact_no',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('Male', 'male'), ('female', 'Female')], default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='UserLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login_date', models.DateTimeField(auto_now=True)),
                ('last_job_apply_date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]