from django import forms
from .models import *
from django.core.files.storage import FileSystemStorage

class DateTimeInput(forms.DateTimeInput):
    input_type = 'date'


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fs = FileSystemStorage(location='gym_manager_project/apps/static/assets/health_files')
        fields = ('name','last_name','dni','phone','email','health_file','emergency_contact','suscription','date')
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'last_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'dni' : forms.NumberInput(attrs={'class': 'form-control'}),
            'phone' : forms.NumberInput(attrs={'class': 'form-control'}),
            'email' : forms.EmailInput(attrs={'class': 'form-control'}),
            'health_file' : forms.FileInput(attrs={'class': 'form-control'}),
            'emergency_contact' : forms.NumberInput(attrs={'class': 'form-control'}),
            'suscription' : forms.Select(attrs={'class': 'form-control'}),
            'date' : DateTimeInput(),

        }

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fs = FileSystemStorage(location='gym_manager_project/apps/static/assets/health_files')
        fields = ('name','last_name','dni','phone','email','health_file')
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'last_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'dni' : forms.NumberInput(attrs={'class': 'form-control'}),
            'phone' : forms.NumberInput(attrs={'class': 'form-control'}),
            'email' : forms.EmailInput(attrs={'class': 'form-control'}),
            'health_file' : forms.FileInput(attrs={'class': 'form-control'}),
        }
        
class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ('name','muscle','link')
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'muscle' : forms.TextInput(attrs={'class': 'form-control'}),
            'link' : forms.TextInput(attrs={'class': 'form-control'}),
            
        }