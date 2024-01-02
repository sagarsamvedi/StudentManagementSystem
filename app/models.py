from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length = 200)
    email = models.EmailField(max_length = 200)
    password = models.CharField(max_length = 250)

    def __str__(self):
        return self.name

class Course(models.Model):
    course_name = models.CharField(max_length = 200)
    fees = models.IntegerField()
    duration = models.CharField(max_length= 200)
    desc = models.TextField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.course_name


class Student(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=250)
    phone = models.CharField(max_length=10)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    college = models.CharField(max_length= 200)
    degree = models.CharField(max_length= 200)
    comment = models.TextField()
    profile_pic = models.ImageField(upload_to='student')

    def __str__(self):
        return self.name
