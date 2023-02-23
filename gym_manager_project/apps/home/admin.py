# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import Staff,Student,Suscripcion,Exercise,Routines,Payments,RestTime,Reps,Day
# Register your models here.
admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(Suscripcion)
admin.site.register(Exercise)
admin.site.register(Routines)
admin.site.register(Payments)
admin.site.register(Day)
admin.site.register(RestTime)
admin.site.register(Reps)

