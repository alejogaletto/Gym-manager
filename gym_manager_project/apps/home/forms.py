from django import forms
from .models import *
from django.core.files.storage import FileSystemStorage

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fs = FileSystemStorage(location='gym_manager_project/apps/static/assets/health_files')
        fields = ('name','last_name','dni','phone','email','health_file','emergency_contact','suscription')
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'last_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'dni' : forms.NumberInput(attrs={'class': 'form-control'}),
            'phone' : forms.NumberInput(attrs={'class': 'form-control'}),
            'email' : forms.EmailInput(attrs={'class': 'form-control'}),
            'health_file' : forms.FileInput(attrs={'class': 'form-control'}),
            'emergency_contact' : forms.NumberInput(attrs={'class': 'form-control'}),
            'suscription' : forms.Select(attrs={'class': 'form-control'}),

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

class RutineForm(forms.Form):
    exc_name = forms.CharField(
        label="Ejercicio",
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )

    reps = forms.CharField(
        label="Repeticiones",
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )

    rest = forms.CharField(
        label="Descanso",
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )