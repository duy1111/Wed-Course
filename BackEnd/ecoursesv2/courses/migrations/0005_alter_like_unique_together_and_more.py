# Generated by Django 4.1.3 on 2022-11-16 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_remove_lesson_viewers_remove_like_created_date_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='like',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together=set(),
        ),
    ]