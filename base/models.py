from django.db import models

# Create your models here.


class Departments(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=255)


    class Meta:
        verbose_name_plural = 'Departments'


class Employees(models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=255)
    Department = models.CharField(max_length=255)
    DateOfJoining = models.DateField()
    PhotoFileName = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = 'Employees'