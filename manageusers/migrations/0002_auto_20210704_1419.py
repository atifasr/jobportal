# Generated by Django 3.2.4 on 2021-07-04 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manageusers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_type',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=255, verbose_name='email address'),
        ),
    ]