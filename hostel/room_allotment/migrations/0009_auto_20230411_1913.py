# Generated by Django 3.2.6 on 2023-04-11 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room_allotment', '0008_remove_student_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hostel',
            name='id',
        ),
        migrations.AlterField(
            model_name='hostel',
            name='hostel_id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
