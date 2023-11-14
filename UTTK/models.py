from django.db import models

# Create your models here.

class Student(models.Model):
    studentID = models.CharField(max_length=50, primary_key=True)
    studentName = models.CharField(max_length=50)
    studentClass = models.CharField(max_length=50)  # Add the studentClass field
    studentEmail = models.CharField(max_length=30)
    studentPhone = models.CharField(max_length=15)

class UTTK_Member(models.Model):
    uttkID = models.CharField(max_length=50, primary_key=True)
    uttkName = models.CharField(max_length=50)
    uttkPhone = models.CharField(max_length=15)
    uttkEmail = models.CharField(max_length=30)
    uttkPass = models.CharField(max_length=60, default="null")

class Lecturer(models.Model):
    lecID = models.CharField(max_length=50, primary_key=True)
    lecName = models.CharField(max_length=50)
    lecPhone = models.CharField(max_length=15)
    lecEmail = models.CharField(max_length=30)
    lecPass = models.CharField(max_length=60, default="null")

class Register_Case(models.Model):
    caseCode = models.CharField(max_length=50, primary_key=True)
    caseClass = models.CharField(max_length=50)
    offences = models.TextField(max_length=500)
    punishment = models.TextField(max_length=500)
    registerText = models.TextField(max_length=500)

class Disciplinary_Case(models.Model):
    studentName = models.CharField(max_length=50)
    studentID = models.ForeignKey(Student, on_delete=models.CASCADE)
    studentClass = models.CharField(max_length=50)  # Add the studentClass field
    caseCode = models.ForeignKey(Register_Case, on_delete=models.CASCADE)
    disciplinaryText = models.TextField(max_length=500)
    disciplinaryDate = models.DateField()