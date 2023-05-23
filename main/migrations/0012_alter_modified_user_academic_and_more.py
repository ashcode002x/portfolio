# Generated by Django 4.2.1 on 2023-05-20 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_academic_education_internships_links_position_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modified_user',
            name='academic',
            field=models.ManyToManyField(blank=True, to='main.academic', verbose_name='academic'),
        ),
        migrations.AlterField(
            model_name='modified_user',
            name='academic_project',
            field=models.ManyToManyField(blank=True, to='main.project', verbose_name='project'),
        ),
        migrations.AlterField(
            model_name='modified_user',
            name='education',
            field=models.ManyToManyField(blank=True, to='main.education', verbose_name='education'),
        ),
        migrations.AlterField(
            model_name='modified_user',
            name='internships',
            field=models.ManyToManyField(blank=True, to='main.internships', verbose_name='internships'),
        ),
        migrations.AlterField(
            model_name='modified_user',
            name='links',
            field=models.ManyToManyField(blank=True, to='main.links', verbose_name='link'),
        ),
        migrations.AlterField(
            model_name='modified_user',
            name='position',
            field=models.ManyToManyField(blank=True, to='main.position', verbose_name='position'),
        ),
        migrations.AlterField(
            model_name='modified_user',
            name='skill',
            field=models.ManyToManyField(blank=True, to='main.skill', verbose_name='skill'),
        ),
    ]
