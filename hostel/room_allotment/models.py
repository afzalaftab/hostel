from django.db import models
# from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.

class Student(AbstractUser):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('NB','Non-Binary')
        )
    username=None
    is_superuser = None
    is_staff=None
    is_active=None
    date_joined=None
    last_login=None
    email=None
    sex=models.CharField(choices=GENDER_CHOICES,max_length=10);
    password = models.CharField(max_length=100,unique=True)
    # email = models.EmailField(unique=True)
    dateOfBirth = models.DateField(blank=True,null=True)
    # name = models.CharField(max_length=100)
    hostelID=models.CharField(max_length=100,null=True)
    roomNO=models.IntegerField(null=True)
    student_phone=models.CharField(max_length=10);
    studentID=models.CharField(primary_key=True, max_length=20)
    yearOfStudy=models.IntegerField()
    USERNAME_FIELD = 'password'
    REQUIRED_FIELDS = ['student_id']

    def _str_(self):
        return self.student_id   
    class Meta:
        db_table = "student"
class Hostel(models.Model):
    hostel_id=models.CharField(max_length=20,primary_key=True)
    hostel_name=models.CharField(max_length=100)
    hostel_capacity=models.IntegerField()
    def _str_(self):
        return self.hostel_name
    class Meta:
        db_table="hostel"

# class room(models.model):
#     hostel_id = models.ForeignKey(hostel, on_delete=models.CASCADE)
#     room_number=models.IntegerField()
#     number_of_occupants= models.IntegerField(default=1)


