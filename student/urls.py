from django.urls import path
from . views import *
from django.conf.urls.static import static
from django.conf import settings

app_name = 'student'

urlpatterns = [
    path('',loginme),
    path('loginstudent/',loginstudent,name = 'loginstudent'),
    path('dashboard/',dashboard,name = 'dashboard'),
    path('uploadassignment/',uploadassignment, name = 'uploadassignment'),
]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)