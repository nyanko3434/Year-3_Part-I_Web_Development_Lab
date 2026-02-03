from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/list/', views.ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
]