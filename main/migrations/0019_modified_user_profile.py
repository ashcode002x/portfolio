# Generated by Django 4.2.1 on 2023-05-23 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_alter_internships_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='modified_user',
            name='profile',
            field=models.ImageField(blank=True, upload_to='userprofile/'),
        ),
    ]
