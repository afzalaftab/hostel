from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='hostel-home'),
    path('profile/', views.profile, name='profile'),
    path('allot/', views.allot, name='allot'),
]
