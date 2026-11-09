from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home/index.html')

def student_dashboard(request):
    return render(request, 'students/student-dashboard.html')

def add_student(request):
    return render(request, 'students/add-student.html')

def edit_student(request):
    return render(request, 'students/edit-student.html')

def students(request):
    return render(request, 'students/')