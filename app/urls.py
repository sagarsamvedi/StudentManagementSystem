from django.urls import path
from . views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',index),
    path('courses/',courses),
    path('dashboard/',dashboard),
    path('profile/',profile),
    path('signup/',signup),
    path('viewstudents/',viewstudents),
    path('register/',register),
    path('login/',login),
    path('addcourses/',addCourse),
    path('createstudent/',createStudent),
    path('updatecourse/<int:pk>',updateCourse,name = "updatecourse"),
    path('deletecourse/<int:pk>/',deleteCourse, name = 'deletecourse'),
    path('updateCourseDetail/',updateCourseDetail),
    path('searchCourse/',searchCourse),
    path('viewProfile/<int:pk>/',viewProfile, name = "viewProfile"),

]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
