# Generated by Django 3.2.5 on 2021-09-16 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_management', '0020_rename_zip_joblocation_zip_code'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobpost',
            old_name='salary',
            new_name='salary_end',
        ),
        migrations.AddField(
            model_name='jobpost',
            name='salary_start',
            field=models.DecimalField(decimal_places=2, default=100000, max_digits=10),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='job_skillset',
            name='skill',
        ),
        migrations.AddField(
            model_name='job_skillset',
            name='skill',
            field=models.ManyToManyField(to='job_management.Skillset'),
        ),
    ]
