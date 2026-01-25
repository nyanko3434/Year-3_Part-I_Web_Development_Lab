from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add-student/', views.add_student, name='add-student'),
    path('edit-student/<int:student_id>/', views.edit_student, name='edit-student'),
]