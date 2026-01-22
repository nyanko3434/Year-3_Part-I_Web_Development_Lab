from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    print (request)
    print (request.method)
    print (request.headers)
    return render(request, 'student_app/index.html', {'name': 'Student Management System'})