# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

class Suscripcion(models.Model):
    """
        Data related to suscripotion
    """
    PLAN_OPT = [
        ("2XW", "Two times a week"),
        ("3XW", "Three timees a week"),
        ("UNL", "Unlimited")
    ]
    tipo_plan = models.CharField(max_length=3,choices=PLAN_OPT)
    estado = models.BooleanField(default=False)
    dia_vencimiento = models.DateTimeField()


class Student(models.Model):
    """
        All data related to the gym students 
    """
    name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    dni = models.IntegerField(max_length=8, null=True)
    phone = models.IntegerField(max_length=15, null=True)
    email = models.EmailField(null=True)
    emergency_contact = models.IntegerField(max_length=15, null=True)
    health_file = models.FileField()
    suscription = models.ForeignKey(Suscripcion, related_name="susccription", on_delete=models.CASCADE)
    
class Staff(models.Model):
    name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    dni = models.IntegerField(max_length=8, null=True)
    phone = models.IntegerField(max_length=15, null=True)
    email = models.EmailField(null=True)
    
class Payments(models.Model):
    METHOD_OPT = [
        ("E", "Cash"),
        ("C", "Credit card"),
        ("D", "Debit card")
    ]
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    date = models.DateTimeField()
    method = models.CharField(max_length=1,choices=METHOD_OPT)
    staff = models.ForeignKey(Staff,on_delete=models.CASCADE)

class Exercise(models.Model):
    name = models.CharField(max_length=30, null=True)
    muscle = models.CharField(max_length=30, null=True)
    
class Routines(models.Model):
    exercises = models.ForeignKey(Exercise,on_delete=models.CASCADE)
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
 
    
