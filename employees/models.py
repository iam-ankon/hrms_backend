from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('hr', 'HR'),
        ('employee', 'Employee'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='employee')

class EmployeeProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    position = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    date_joined = models.DateField(auto_now_add=True)

class Attendance(models.Model):
    employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('present', 'Present'), ('absent', 'Absent')])

class LeaveRequest(models.Model):
    employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=10, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending')

class Payroll(models.Model):
    employee = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    month = models.CharField(max_length=20)
    salary_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField(auto_now_add=True)
