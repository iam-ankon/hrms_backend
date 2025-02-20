from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db import models

class Employee(models.Model):
    EMPLOYEE_STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
        ('Terminated', 'Terminated'),
    ]
    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # Updated
    employee_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    joining_date = models.DateField()
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=EMPLOYEE_STATUS_CHOICES, default='Active')
    profile_picture = models.ImageField(upload_to='employees/', null=True, blank=True)

    def __str__(self):
        return self.name


class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    check_in = models.TimeField()
    check_out = models.TimeField(null=True, blank=True)
    is_late = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.employee.name} - {self.date}"

class Leave(models.Model):
    LEAVE_TYPE_CHOICES = [
        ('Sick Leave', 'Sick Leave'),
        ('Earned Leave', 'Earned Leave'),
        ('Casual Leave', 'Casual Leave'),
    ]
    
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=50, choices=LEAVE_TYPE_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending')

    def __str__(self):
        return f"{self.employee.name} - {self.leave_type}"

class Payroll(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    month = models.CharField(max_length=20)
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2)
    tax_deductions = models.DecimalField(max_digits=10, decimal_places=2)
    net_salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.employee.name} - {self.month}"

class PerformanceReview(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    review_date = models.DateField()
    rating = models.PositiveIntegerField()  # 1-5 scale
    feedback = models.TextField()

    def __str__(self):
        return f"{self.employee.name} - {self.review_date}"

class Training(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    training_name = models.CharField(max_length=255)
    training_date = models.DateField()
    status = models.CharField(max_length=50, choices=[('Pending', 'Pending'), ('Completed', 'Completed')])

    def __str__(self):
        return f"{self.employee.name} - {self.training_name}"

class Compliance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    policy_name = models.CharField(max_length=255)
    compliance_status = models.CharField(max_length=50, choices=[('Compliant', 'Compliant'), ('Non-Compliant', 'Non-Compliant')])
    last_updated = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.employee.name} - {self.policy_name}"
