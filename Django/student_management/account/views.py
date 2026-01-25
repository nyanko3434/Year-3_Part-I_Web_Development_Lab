from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import RegistrationForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password1']
            )
            user.save()
            # Redirect to a success page or login page
            if user:
                return HttpResponseRedirect('/account/login/')
            
    return render(request, 'account/registration.html', {'form': form})

def login_view(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Authenticate user logic here
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/student/')
            else:
                return HttpResponse("Invalid credentials")

            # Redirect to dashboard or home page on success

    return render(request, 'account/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/account/login/')