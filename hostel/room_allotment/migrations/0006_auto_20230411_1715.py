# Generated by Django 3.2.6 on 2023-04-11 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room_allotment', '0005_auto_20230411_1245'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='date_of_birth',
            new_name='dateOfBirth',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='hostel_name',
            new_name='hostelID',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='room_number',
            new_name='roomNO',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='student_id',
            new_name='studentID',
        ),
    ]