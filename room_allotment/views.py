from django.shortcuts import render
from .models import *
from django.db import connection
# Create your views here.
from .models import Hostel
from django.contrib.auth import login , logout
def home(request):
    return render(request, 'hostel_allotment/home.html', {'title':'home'})
def profile(request):
    if request.method == "POST":
        stud_id = request.POST.get("username")
        password = request.POST.get("password")
        student = Student.objects.raw(f"select * from student where studentID={stud_id} and password='{password}'")[0]
        login(request, student)
    context = {"student":request.user}
    return render(request,'hostel_allotment/profile.html',context=context)
def allot(request):
    cursor = connection.cursor()
    if request.method == "POST":
        hostel1 = Hostel.objects.get(hostel_name=request.POST.get("hostel"))
        cursor.execute(f"update student set hostelID={hostel1.pk} where studentID={request.user.pk};")
        cursor.execute(f"update student set roomNo=(select RoomNo from room where noOfOccupants<2 and hostelID={hostel1.pk}) where studentID = {request.user.pk}; ")
        context = {"student":request.user}
        return render(request,'hostel_allotment/profile.html',context=context)
    cursor.execute("select * from hostel")
    hostel = cursor.fetchall()
    print(hostel)
    context = {}
    context["hostel"] = hostel

    return render(request, 'hostel_allotment/allot.html', context=context)