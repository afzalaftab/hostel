# Generated by Django 3.2.6 on 2023-04-11 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room_allotment', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='student',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='student',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='student',
            name='is_superuser',
        ),
    ]
