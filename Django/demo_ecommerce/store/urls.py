from django.urls import include, path
from . import views

urlpatterns = [
    # Define your app-specific URL patterns here
    path('', views.home, name='home'),
    path("add_product/",views.add_product,name="add_product"),
]