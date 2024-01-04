from django.shortcuts import render, redirect
from app.models import Teacher
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.


def login(request):
    return render(request, 'login.html')


def teacherLogin(request):
    if request.method == "POST":
        mobile = request.POST.get('phone')
        password = request.POST.get('password')
        if Teacher.objects.filter(phone=mobile).exists():
            obj = Teacher.objects.get(phone=mobile)
            db_password = obj.password
            if check_password(password, db_password):
                return redirect("dashboard/")
            else:
                return HttpResponse('Password Failed')

        else:
            return HttpResponse('Mobile Number not Exists')


def dashboard_user(request):
    return render(request, 'dashboard.html')
