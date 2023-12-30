from django.urls import path
from . views import *

urlpatterns = [
    path('',index),
    path('courses/',courses),
    path('dashboard/',dashboard),
    path('profile/',profile),
    path('signup/',signup),
    path('viewstudents/',viewstudents),
    path('register/',register),
    path('login/',login)
]
