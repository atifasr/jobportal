# Generated by Django 3.2.5 on 2021-09-14 03:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companyprofile', '0006_auto_20210913_2215'),
        ('manageusers', '0013_user_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='companyprofile.company'),
        ),
    ]