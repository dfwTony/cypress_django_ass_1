from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm


# Show all students in a table
def index(request):
    students = Student.objects.all()
    return render(request, 'students/index.html', {'students': students})


# Show the details of one student
def view_student(request, id):
    student = get_object_or_404(Student, pk=id)
    return render(request, 'students/view.html', {'student': student})


# Add a new student
def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = StudentForm()
    return render(request, 'students/add.html', {'form': form})


# Edit an existing student
def edit(request, id):
    student = get_object_or_404(Student, pk=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/edit.html', {'form': form, 'student': student})


# Delete a student (only when the form is submitted with POST)
def delete(request, id):
    student = get_object_or_404(Student, pk=id)
    if request.method == 'POST':
        student.delete()
    return redirect('index')
