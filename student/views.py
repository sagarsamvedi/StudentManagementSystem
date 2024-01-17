from django.shortcuts import render,redirect
from app.models import *
from teacher.models import *
from django.http import HttpResponse

# Create your views here.

def loginme(request):
    return render(request,'studentapp/login.html')

def loginstudent(request):
    if request.method == "POST":
        mobile = request.POST.get('phone')
        password = request.POST.get('password')
        print(password)
        if Student.objects.filter(phone=mobile).exists():
            obj = Student.objects.get(phone=mobile)
            request.session["phone"] = obj.phone
            if password == obj.password:
                return redirect("student:dashboard")
            else:
                return HttpResponse('Password Failed')
        else:
            return HttpResponse('Mobile Number not Exists')

def dashboard(request):
    student_phone = request.session.get("phone")

    if student_phone:
        student = Student.objects.get(phone = student_phone)
        return render(request, 'studentapp/dashboard.html',{'student':student})
    else:
        return HttpResponse('Student not logged in')
    
def uploadassignment(request):
    assignments = Assignment.objects.all()
    return render(request,'studentapp/uploadassignment.html',{'assignments':assignments})
