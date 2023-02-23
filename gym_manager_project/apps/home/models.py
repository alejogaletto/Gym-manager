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
    def __str__(self) -> str:
        return self.tipo_plan


class Student(models.Model):
    """
        All data related to the gym students 
    """
    SUSCRIPTION_OPTS = [
        (100, "UNL"),
        (12, "3XW"),
        (8,"2XW"),
    ]

    name = models.CharField('Nombre',max_length=30, null=True)
    last_name = models.CharField('Apellido',max_length=30, null=True)
    dni = models.IntegerField('DNI',max_length=8, null=True)
    phone = models.IntegerField('Teléfono',max_length=15, null=True)
    email = models.EmailField('Email',null=True)
    emergency_contact = models.IntegerField('Contacto de emergencia',max_length=15, null=True)
    health_file = models.FileField('Ficha medica', upload_to="health_files")
    suscription = models.IntegerField(max_length=3,choices=SUSCRIPTION_OPTS)
    date = models.DateTimeField(auto_now_add=True)
    routine = models.FileField('Plan de entrenamiento', upload_to="rutines", null=True)
    routine_st = models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.name + " " + self.last_name  

class Staff(models.Model):
    name = models.CharField('Nombre', max_length=30, null=True)
    last_name = models.CharField('Apellido',max_length=30, null=True)
    dni = models.IntegerField('DNI',max_length=8, null=True)
    phone = models.IntegerField('Teléfono',max_length=15, null=True)
    email = models.EmailField('Email',null=True)
    health_file = models.FileField('Ficha médica',null=True)

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

class Reps(models.Model):
    reps = models.CharField(max_length=30, null=True)

class RestTime(models.Model):
    restTime= models.CharField(max_length=30, null=True)

class Exercise(models.Model):
    name = models.CharField('Nombre', max_length=30, null=True)
    muscle = models.CharField('Músculo',max_length=30, null=True)
    link = models.CharField('Link de video', max_length=100,null=True)
    
class Day(models.Model):
    name = models.CharField("Dia", max_length=50, null=True)
    exercise = models.ManyToManyField(Exercise)
    reps = models.ManyToManyField(Reps)
    restTime = models.ManyToManyField(RestTime)
class Routines(models.Model):
    student = models.ForeignKey(Student,on_delete=models.CASCADE)
    day = models.ManyToManyField(Day)

    

    

