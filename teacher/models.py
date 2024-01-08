from django.db import models
from app.models import *

# Create your models here.


class Assignment(models.Model):
    STATUS_CHOICES = (
        ('done', 'Done'),
        ('pending', 'Pending'),
    )

    assignment_name = models.CharField(max_length=250)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    marks = models.IntegerField()
    assignment_file = models.FileField(upload_to='docs/', null=True)
    assign_students = models.ManyToManyField(Student, blank=True, null=True)
    assignment_course = models.ForeignKey(Course, on_delete=models.CASCADE)
    assignment_desc = models.TextField()

    def __str__(self):
        return self.assignment_name

