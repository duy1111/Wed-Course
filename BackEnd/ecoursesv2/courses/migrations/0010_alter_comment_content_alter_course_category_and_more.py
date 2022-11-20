# Generated by Django 4.1.3 on 2022-11-17 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_course_pre_courses_lesson_viewers_like_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.category'),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='pre_courses',
            field=models.ManyToManyField(null=True, to='courses.course'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rate',
            field=models.SmallIntegerField(default=0),
        ),
    ]