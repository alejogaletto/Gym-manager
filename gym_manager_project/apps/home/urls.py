# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.views.generic import RedirectView
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
    path("staff/create",StaffCreate.as_view() ,name = "staffCreate"),
    path("staff/<pk>",StaffUpdate.as_view() ,name = "staffDetail"),
    path("staff/delete/<pk>",StaffDelete.as_view() ,name = "deleteStaff"),
    path("exercise/create",ExerciseCreate.as_view() ,name = "exerciseCreate"),
    path("exercise/<pk>",ExerciseUpdate.as_view() ,name = "exerciseDetail"),
    path("exercise/delete/<pk>",ExerciseDelete.as_view() ,name = "deleteExercise"),
    path("studentLogIn/",studentLogIn ,name = "studentLogIn"),
    path(r'^favicon\.ico$',RedirectView.as_view(url='/static/images/favicon.ico'))
]


urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
