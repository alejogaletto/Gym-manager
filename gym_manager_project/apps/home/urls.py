# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path("home/", views.pages,name = "pages"),
    path("students/",students,name = "students"),
    path("staff/",staff,name = "staff"),
    path("exercises/",exercises,name = "exercises"),
    path("payments/",payments ,name = "payments"),
    path("students/create",StudentCreate.as_view() ,name = "studentCreate"),
    path("students/<pk>",StudentUpdate.as_view() ,name = "studentDetail"),
    path("students/delete/<pk>",StudentDelete.as_view() ,name = "deleteStudent"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
