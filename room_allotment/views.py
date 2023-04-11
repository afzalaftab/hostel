from django.shortcuts import render
from .models import *
from django.db import connection
# Create your views here.
from django.contrib.auth import login , logout
def home(request):
    return render(request, 'hostel_allotment/home.html', {'title':'home'})
def profile(request):
    if request.method == "POST":
        stud_id = request.POST.get("username")
        password = request.POST.get("password")
        student = Student.objects.raw(f"select * from student where student_id={stud_id} and password='{password}'")[0]
        login(request, student)
    context = {"student":request.user}
    return render(request,'hostel_allotment/profile.html',context=context)