from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings

# Email Log Model
class EmailLog(models.Model):
    recipient = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Email to {self.recipient} at {self.sent_at}"

# Emergency Contact Model
class EmergencyContact(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.name

# Employee Details Model
class EmployeeDetails(models.Model):
    employee_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    joining_date = models.DateField()
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    mail_address = models.TextField()
    personal_phone = models.CharField(max_length=20)
    office_phone = models.CharField(max_length=20)
    reference_phone = models.CharField(max_length=20, blank=True, null=True)
    job_title = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    office_in_time = models.TimeField()
    office_out_time = models.TimeField()
    attendance_delay = models.BooleanField(default=False)
    earned_leave = models.IntegerField(default=0)
    sick_leave = models.IntegerField(default=0)
    leave_description = models.TextField(blank=True, null=True)
    birthday = models.DateField()
    reporting_leader = models.CharField(max_length=255)
    special_skills = models.TextField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    image1 = models.ImageField(upload_to='employee_images/')
    image2 = models.ImageField(upload_to='employee_images/', blank=True, null=True)
    office_regular_time = models.TimeField()
    office_grace_time = models.TimeField()
    employee_address = models.TextField()
    emergency_contact = models.OneToOneField(EmergencyContact, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# Notification Model
class Notification(models.Model):
    employee = models.ForeignKey(EmployeeDetails, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.employee.name}"

# Auto-generate notification and send email
@receiver(post_save, sender=EmployeeDetails)
def create_notification(sender, instance, **kwargs):
    if instance.attendance_delay:
        message = f"Attendance delay recorded for {instance.name} on {instance.joining_date}."
        
        # Create Notification
        notification = Notification.objects.create(employee=instance, message=message)
        
        # Send Email
        send_mail(
            subject="Attendance Delay Alert",
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[instance.email],
            fail_silently=True
        )

        # Log Email
        EmailLog.objects.create(
            recipient=instance.email,
            subject="Attendance Delay Alert",
            message=message
        )