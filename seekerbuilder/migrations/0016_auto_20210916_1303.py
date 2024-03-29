# Generated by Django 3.2.5 on 2021-09-16 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_management', '0019_auto_20210913_2147'),
        ('seekerbuilder', '0015_auto_20210914_1503'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='educationdetail',
            options={'verbose_name_plural': "Seekers' education details"},
        ),
        migrations.AlterModelOptions(
            name='experiencedetail',
            options={'verbose_name_plural': "Seekers' experience details"},
        ),
        migrations.AlterModelOptions(
            name='seekerprofile',
            options={'verbose_name_plural': "Seekers' profile"},
        ),
        migrations.AlterModelOptions(
            name='seekerskillset',
            options={'verbose_name': 'Seeker skill set', 'verbose_name_plural': "Seeker's skills"},
        ),
        migrations.RemoveField(
            model_name='seekerskillset',
            name='skill_set',
        ),
        migrations.AddField(
            model_name='seekerskillset',
            name='skill_set',
            field=models.ManyToManyField(to='job_management.Skillset'),
        ),
    ]
