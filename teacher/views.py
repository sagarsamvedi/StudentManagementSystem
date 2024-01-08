from django.shortcuts import render, redirect
from app.models import Teacher, Student
from . models import *
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.


def loginus(request):
    return render(request, 'login.html')


def teacherLogin(request):
    if request.method == "POST":
        mobile = request.POST.get('phone')
        password = request.POST.get('password')
        if Teacher.objects.filter(phone=mobile).exists():
            obj = Teacher.objects.get(phone=mobile)
            db_password = obj.password
            if check_password(password, db_password):
                return redirect("teacher:dashboard_user")
            else:
                return HttpResponse('Password Failed')

        else:
            return HttpResponse('Mobile Number not Exists')


def dashboard_user(request):
    # students = Student.objects.filter(course_name = )
    return render(request, 'teacherapp/dashboard.html')


def assignment(request):
    assignments = Assignment.objects.all()
    courses = Course.objects.all()
    students = Student.objects.all()
    status_choices = get_status_choices()
    return render(request, 'teacherapp/assignment.html', {"assignments": assignments, "students": students, "courses": courses, "status_choices": status_choices})


def get_status_choices():
    return Assignment.STATUS_CHOICES


def createassignment(request):
    if request.method == 'POST':
        assignment_name = request.POST.get('assignment_name')
        status = request.POST.get('status')
        marks = request.POST.get('marks')
        assign_students_ids = request.POST.get('assign_students')
        assignment_course_id = request.POST.get('assignment_course')
        assignment_desc = request.POST.get('assignment_desc')
        assignment_file = request.FILES.get('assignment_file')

        # Step 1: Get the related objects
        assignment_course = Course.objects.get(id=assignment_course_id)
        assign_students = Student.objects.filter(id__in=assign_students_ids)

        # Step 2: Create the Assignment object
        assignment = Assignment.objects.create(
            assignment_name=assignment_name,
            status=status,
            marks=marks,
            assignment_file=assignment_file,
            assignment_course=assignment_course,
            assignment_desc=assignment_desc
        )

        # Add the many-to-many relationship
        assignment.assign_students.set(assign_students)

        # Save the changes
        assignment.save()

        
    return redirect("teacher:assignment")
