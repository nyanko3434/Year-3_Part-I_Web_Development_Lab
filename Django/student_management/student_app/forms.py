from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'enrollment_number', 'date_of_birth', 'email']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }