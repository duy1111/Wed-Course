# Generated by Django 4.1.3 on 2022-11-10 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_course_pre_courses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='pre_courses',
        ),
        migrations.DeleteModel(
            name='CVOnline',
        ),
    ]
