# Generated by Django 3.2.5 on 2021-07-21 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companyprofile', '0004_alter_companyimage_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companyimage',
            old_name='image',
            new_name='images',
        ),
        migrations.AddField(
            model_name='companyimage',
            name='cover_image',
            field=models.ImageField(default='C:\\Users\\atif\\Downloads\\1626264705038.jpg', upload_to='images/company_cover'),
            preserve_default=False,
        ),
    ]
