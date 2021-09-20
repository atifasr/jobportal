# Generated by Django 3.2.5 on 2021-09-13 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companyprofile', '0005_auto_20210721_1514'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='stream',
        ),
        migrations.AddField(
            model_name='buisnessstream',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='companyprofile.company'),
        ),
    ]