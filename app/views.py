from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import *
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from django.db.models import Q
# Create your views here.


def courses(request):
    courses = Course.objects.all()
    return render(request, 'courses.html', {"courses": courses})


def dashboard(request):
    courses = Course.objects.all()
    course_count = Course.objects.count()
    student_count = Student.objects.count()
    return render(request, 'dashboard.html', {"courses": courses, "courses_count": course_count, "student_count": student_count})


def index(request):
    return render(request, 'index.html')


def profile(request):
    return render(request, 'profile.html')


def signup(request):
    return render(request, 'sign-up.html')


def viewstudents(request):
    students = Student.objects.all()
    courses = Course.objects.all()
    return render(request, 'viewstudents.html', {"students": students, "courses": courses})


def register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(email=email).exists():
            return HttpResponse("Email already Exists")
        elif isStrongPassword(password):
            User.objects.create(name=name, email=email,
                                password=make_password(password))
            return HttpResponse("User created successfully")
        else:
            return HttpResponse("Use Strong Password")


def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        user_password = request.POST.get('password')

        if User.objects.filter(email=email).exists():
            user_obj = User.objects.get(email=email)
            Password = user_obj.password

            if check_password(user_password, Password):
                return redirect('/dashboard/')
            else:
                return HttpResponse("Invalid Password")
        else:
            return HttpResponse("Email not exist")


def isStrongPassword(password):
    special_chars = "!@#$%&"
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char in special_chars for char in password):
        return False
    # If all checks pass, the password is considered strong
    return True


def addCourse(request):
    if request.method == 'POST':
        course_name = request.POST.get("course")
        fees = request.POST.get("fees")
        duration = request.POST.get("duration")
        desc = request.POST.get("desc")

        if Course.objects.filter(course_name=course_name).exists():
            messages.error(request, "Course Already Exist")
            return redirect('/courses/')
        else:
            Course.objects.create(course_name=course_name,
                                  fees=fees, duration=duration, desc=desc)
            messages.success(request, "Course Successfully Created")
            return redirect('/courses/')


def createStudent(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")

        college = request.POST.get("college")
        degree = request.POST.get("degree")
        course_id = request.POST.get("course")
        comment = request.POST.get("comment")
        profile_pic = request.FILES.get("profilepic")

        # Check if a student with the same email already exists
        if Student.objects.filter(email=email).exists():
            messages.error(request, "Student with this email already exists.")
            return redirect('/viewstudents/')

        stud = Course.objects.get(id=course_id)

        # Create the student object
        Student.objects.create(
            name=name,
            email=email,
            course=stud,
            phone=phone,
            college=college,

            degree=degree,
            comment=comment,
            profile_pic=profile_pic,
        )
        messages.success(request, "Student created successfully.")
        return redirect('/viewstudents/')

def updateCourse(request, pk):
    course = Course.objects.get(id=pk)
    return render(request, 'updatecourse.html', {"course": course})


def deleteCourse(request, pk):
    Course.objects.get(id=pk).delete()
    return redirect('/courses/')


def updateCourseDetail(request):
    if request.method == "POST":
        course_name = request.POST.get("course")
        fees = request.POST.get("fees")
        duration = request.POST.get("duration")
        desc = request.POST.get("desc")
        course_id = request.POST.get("id")

        Course.objects.filter(id=course_id).update(
            course_name=course_name, fees=fees, duration=duration, desc=desc
        )
        return redirect('/courses/')


def searchCourse(request):
    if "q" in request.GET:
        q = request.GET["q"]
        multiple_q = Q(Q(course_name__icontains=q) | Q(
            fees__icontains=q) | Q(duration__icontains=q))
        course = Course.objects.filter(multiple_q)
    else:
        course = Course.objects.all()
    return render(request, 'courses.html', {"courses": course})


def viewProfile(request, pk):
    student = Student.objects.get(id=pk)
    return render(request, 'profile.html', {"student": student})


def updateStudent(request, pk):
    student = Student.objects.get(id=pk)
    courses = Course.objects.all()
    return render(request, 'updateStudent.html', {"student": student, "courses": courses})


def updateStudentDetail(request):
    if request.method == "POST":
        std_id = request.POST.get("id")
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        college = request.POST.get("college")
        degree = request.POST.get("degree")
        course_id = request.POST.get("course")
        comment = request.POST.get("comment")
        profile_pic = request.FILES.get("profilepic")

        stud = Course.objects.get(id=course_id)

        # Update the student object

        std = Student.objects.get(id=std_id)

        std.name = name
        std.email = email
        std.course = stud
        std.phone = phone
        std.college = college
        std.degree = degree
        std.comment = comment

        if profile_pic:
            std.profile_pic = profile_pic

        std.save()
        return redirect(f'/viewProfile/{std_id}')


def deleteStudent(request, pk):
    Student.objects.get(id=pk).delete()
    return redirect('/viewstudents/')


def searchStudent(request):
    if "studentQuery" in request.GET:
        q = request.GET["studentQuery"]
        students = Student.objects.filter(
            Q(name__icontains=q) |
            Q(email__icontains=q) |
            Q(phone__icontains=q) |
            Q(college__icontains=q) |
            Q(degree__icontains=q)
        )
    else:
        students = Student.objects.all()

    return render(request, 'viewstudents.html', {"students": students})


def viewTeachers(request):
    teachers = Teacher.objects.all()
    courses = Course.objects.all()
    return render(request, 'viewteachers.html', {"teachers": teachers, "courses": courses})


def createTeacher(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        experience = request.POST.get("experience")
        password = request.POST.get("password")
        course_id = request.POST.get("course")
        phone = request.POST.get("phone")
        date_of_joining = request.POST.get("date")
        profilepic = request.FILES.get("profilepic")

        assignedCourse = Course.objects.get(id=course_id)

        Teacher.objects.create(
            name=name,
            email=email,
            phone=phone,
            experience=experience,
            assigned_course=assignedCourse,
            password=make_password(password),
            profile_pic=profilepic,
            date_of_joining=date_of_joining
        )
        return redirect('/viewteachers/')
