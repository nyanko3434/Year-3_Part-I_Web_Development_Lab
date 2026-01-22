from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    print (request)
    print (request.method)
    print (request.headers)
    return HttpResponse("<h1>Welcome to the Student Management System</h1>")