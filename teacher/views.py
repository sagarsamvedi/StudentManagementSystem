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
            request.session["phone"] = obj.phone
            if check_password(password, db_password):
                return redirect("teacher:dashboard_user")
            else:
                return HttpResponse('Password Failed')
        else:
            return HttpResponse('Mobile Number not Exists')


def dashboard_user(request):
    # students = Student.objects.filter(course_name = )
    teacher_phone = request.session.get("phone")

    if teacher_phone:
        teacher = Teacher.objects.get(phone = teacher_phone)
        students = Student.objects.filter(course = teacher.assigned_course)
        return render(request, 'teacherapp/dashboard.html', {"teacher": teacher,"students":students})
    else:
        return HttpResponse('Teacher not logged in')

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
        assign_students_ids = request.POST.getlist('assign_students')
        assignment_course_id = request.POST.get('assignment_course')
        assignment_desc = request.POST.get('assignment_desc')
        assignment_file = request.FILES.get('assignment_file')
        print(assign_students_ids)
        # Step 1: Get the related objects
        assignment_course = Course.objects.get(id=assignment_course_id)
        assign_students = Student.objects.filter(id__in=assign_students_ids)
        print(assign_students)
        
        teacher = Teacher.objects.get(phone=request.session.get('phone'))
        # Step 2: Create the Assignment object
        assignment = Assignment.objects.create(
            assignment_name=assignment_name,
            status=status,
            marks=marks,
            assignment_file=assignment_file,
            assignment_course=assignment_course,
            assignment_desc=assignment_desc,
             uploaded_by=teacher,
        )

        # Add the many-to-many relationship
        assignment.assign_students.set(assign_students)


        # Save the changes
        assignment.save()

        print(assignment)
        return redirect("../assignment")

def deleteassignment(request,pk):
    Assignment.objects.get(id = pk).delete()
    return redirect("../assignment")

def viewstudent(request,pk):
    student = Student.objects.get(id = pk)
    return render(request, 'teacherapp/viewstudent.html', {"student": student})

