# Generated by Django 3.0.1 on 2020-07-17 22:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_delete_course'),
        ('students', '0003_student_level'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Student',
        ),
    ]
