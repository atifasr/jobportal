# Generated by Django 3.2.5 on 2021-09-20 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('job_management', '0028_jobpost_direct_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('jobpost', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='job_management.jobpost')),
            ],
        ),
    ]
