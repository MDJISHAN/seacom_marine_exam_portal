from django.db import models
from django.contrib.auth.models import User
from Exam.student.models import *
#from Exam.admission.models import *
#from Exam.course.models import *
# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=250)
    # Add other student-related fields

class Course(models.Model):
    name = models.CharField(max_length=250)
    credit_units = models.IntegerField()

    # Add other relevant fields and methods for GPA and CGPA calculations

# Views, logic for GPA, CGPA calculations, and updating student profiles would be implemented in views.py

# class Carry_Over_Courses(models.Model):


class ConfigMarks(models.Model):
    mark_score = models.IntegerField()
    grade_letter = models.CharField(max_length=1)
    gp = models.FloatField()

class Score(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    assignment_score = models.FloatField()
    test_score = models.FloatField()
    print("chech",test_score)
    exam_score = models.FloatField()
    print("chech",exam_score)
    print("chech",assignment_score)
    
    is_carry_over = models.BooleanField(default=False)
    attempts = models.IntegerField(default=0)
    
    @property
    def total_score(self):
        return self.assignment_score + self.test_score + self.exam_score
 


