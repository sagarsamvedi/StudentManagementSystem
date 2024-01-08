from django.urls import path
from . views import *
from django.conf.urls.static import static
from django.conf import settings

app_name = 'teacher'

urlpatterns = [
    path('',loginus),
    path('teacherlogin/',teacherLogin, name = 'teacher_login'),
    path('dashboardus/', dashboard_user, name='dashboard_user'),
    path('assignment/', assignment, name='assignment'),
    path('createassignment/', createassignment, name='createassignment'),
]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)