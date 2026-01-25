from django.urls import path
from . import views

urlpatterns = [
    # Define your account-related URL patterns here
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]