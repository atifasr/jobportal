# Generated by Django 3.2.5 on 2021-09-16 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companyprofile', '0007_auto_20210916_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='contact_email',
            field=models.EmailField(default='57-561919', max_length=254),
            preserve_default=False,
        ),
    ]
