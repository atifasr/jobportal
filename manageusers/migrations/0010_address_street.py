# Generated by Django 3.2.5 on 2021-09-13 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manageusers', '0009_auto_20210913_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='street',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
