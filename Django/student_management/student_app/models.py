from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    enrollment_number = models.CharField(max_length=15, unique=True)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.enrollment_number})"

#for python manage.py shell to insert initial data
# python manage.py shell
# from student_app.models import Student, Course

# course1 = Course(course_name="Mathematics", course_code="MATH101", description="Basic Mathematics Course")
# course1.save()    
class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=10, unique=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.course_name} ({self.course_code})"