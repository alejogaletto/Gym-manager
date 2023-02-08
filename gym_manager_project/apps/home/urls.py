# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views
from .views import *


urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path("home/", views.pages,name = "pages"),
    path("students/",students,name = "students"),
    path("staff/",staff,name = "staff"),
    path("exercises/",exercises,name = "exercises"),
    path("payments/",payments ,name = "payments"),
    path("students/create",StudentCreate.as_view() ,name = "studentCreate"),


]

