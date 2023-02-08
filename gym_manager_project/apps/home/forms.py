from django import forms
from .models import *

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        enctype="multipart/form-data"
        fields = ('name','last_name','dni','phone','email','emergency_contact','suscription')
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'last_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'dni' : forms.NumberInput(attrs={'class': 'form-control'}),
            'phone' : forms.NumberInput(attrs={'class': 'form-control'}),
            'email' : forms.EmailInput(attrs={'class': 'form-control'}),
            'emergency_contact' : forms.NumberInput(attrs={'class': 'form-control'}),
            'suscription' : forms.Select(attrs={'class': 'form-control'}),

        }