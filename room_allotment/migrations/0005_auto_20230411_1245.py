# Generated by Django 3.2.6 on 2023-04-11 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room_allotment', '0004_remove_student_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='hostel_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='room_number',
            field=models.IntegerField(null=True),
        ),
    ]
