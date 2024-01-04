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
    path('updatestudent/<int:pk>',updateStudent,name = "updatestudent"),
    path('deletestudent/<int:pk>/',deleteStudent, name = 'deletestudent'),
    path('updateStudentDetail/',updateStudentDetail, name = 'updateStudentDetail'),
    path('searchStudent/',searchStudent),
    path('viewteachers/',viewTeachers),
    path('createteacher/',createTeacher),


]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
