from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('student_dashboard/', views.student_dashboard, name = 'student_dashboard'),
    path('add_student/', views.add_student, name = 'add_student'),
    path('add_student/', views.edit_student, name = 'edit_student'),
    path('students/', views.students, name = 'students'),
    
]