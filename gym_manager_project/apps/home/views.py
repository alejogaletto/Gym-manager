# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse,reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import *
from .forms import StudentForm, StaffForm   






@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

def students(request):
    studentList = Student.objects.all()
    return render(request,'home/students.html',{'studentList' : studentList})

class StudentCreate(CreateView):
    model = Student
    # fields = '__all__'
    form_class = StudentForm
    success_url= reverse_lazy('students')
    template_name= 'home/student_form.html'
    
class StudentUpdate(UpdateView):
    model = Student
    form_class = StudentForm
    success_url= reverse_lazy('students')
    template_name= 'home/student_form.html'

class StudentDelete(DeleteView):
    model = Student
    success_url= reverse_lazy('students')
    template_name= 'home/student_confirm_delete.html'

def staff(request):
    staffList = Staff.objects.all()
    return render(request,'home/staff.html',{'staffList' : staffList})
class StaffCreate(CreateView):
    model = Staff
    form_class = StaffForm
    success_url = reverse_lazy("staff")
    template_name = "home/staff_form.html"

class StaffUpdate(UpdateView):
    model = Staff
    form_class = StaffForm
    success_url= reverse_lazy('staff')
    template_name= 'home/staff_form.html'

class StaffDelete(DeleteView):
    model = Staff
    success_url= reverse_lazy('staff')
    template_name= 'home/staff_confirm_delete.html'


def exercises(request):
    return render(request,'home/exercises.html')

def payments(request):
    return render(request,'home/payments.html')