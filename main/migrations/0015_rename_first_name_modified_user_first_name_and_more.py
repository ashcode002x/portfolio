# Generated by Django 4.2.1 on 2023-05-21 03:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_links_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modified_user',
            old_name='first name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='modified_user',
            old_name='last name',
            new_name='last_name',
        ),
    ]
