from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Student
from .forms import StudentForm

# Create your views here.
# @login_required(login_url='/account/login/')
def index(request):
    print(request.user.username)
    return render(request, 'student_app/index.html', {'name': 'Student Management System'})


def add_student(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        enrollment_number = request.POST.get('enrollment_number')
        date_of_birth = request.POST.get('date_of_birth')
        email = request.POST.get('email')

        # Here you would typically save the student to the database
        # For now, we will just return a success message

        return HttpResponse(f"Student {first_name} {last_name} added successfully!")
    else:
        return render(request, 'student_app/add_student.html')
    
def edit_student(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        return HttpResponse("Student not found", status=404)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return HttpResponse(f"Student {student.first_name} {student.last_name} updated successfully!")
    else:
        form = StudentForm(instance=student)

    return render(request, 'student_app/edit_student.html', {'form': form, 'student_id': student_id})