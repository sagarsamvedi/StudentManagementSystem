from django.db import models
from app.models import *
from teacher.models import *
# Create your models here.

class Student_assignment(models.Model):
    associated_teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment,on_delete=models.CASCADE)
    upload_doc = models.FileField(upload_to='studentdoc/')
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.assignment
