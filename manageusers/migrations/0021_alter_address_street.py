# Generated by Django 3.2.5 on 2021-09-29 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manageusers', '0020_alter_user_contact_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='street',
            field=models.TextField(),
        ),
    ]
