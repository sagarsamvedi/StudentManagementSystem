from django.urls import path
from . views import *

urlpatterns = [
    path('',login),
    path('teacherlogin/',teacherLogin),
    path('dashboard/',dashboard_user),
]