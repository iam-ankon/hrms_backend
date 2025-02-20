from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail,EmailMessage
from django.conf import settings

# Models
class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class CVAdd(models.Model):
    name = models.CharField(max_length=255)
    cv_file = models.FileField(upload_to='cv_adds/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class CV(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="cvs")
    cv_file = models.FileField(upload_to="cvs/")

    def __str__(self):
        return f"{self.name} - {self.department.name}"

class CategorizedCV(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="categorized_cvs")
    cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name="categorized")
    categorized_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cv.name} - {self.department.name}"

class RequirementAnalysis(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    needed_employees = models.IntegerField()
    job_description = models.TextField()

    def __str__(self):
        return f"{self.department.name} - {self.needed_employees} Employees Needed"

class Interview(models.Model):
    candidate = models.ForeignKey(CV, on_delete=models.CASCADE)
    interview_date = models.DateTimeField()
    interview_result = models.TextField()
    interview_notes = models.TextField(blank=True, null=True)
    interview_pdf = models.FileField(upload_to="interviews/", blank=True, null=True)

    def __str__(self):
        return f"Interview - {self.candidate.name}"

class EmployeeDocument(models.Model):
    employee = models.ForeignKey(CV, on_delete=models.CASCADE)
    document_type = models.CharField(
        max_length=50,
        choices=[
            ("offer_letter", "Offer Letter"),
            ("appointment_letter", "Appointment Letter"),
            ("joining_report", "Joining Report"),
        ],
    )
    document_file = models.FileField(upload_to="employee_documents/")
    sent_to_email = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.document_type} for {self.employee.name}"
    
class EmailLog(models.Model):
    recipient = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Email to {self.recipient} at {self.sent_at}"

class ITProvision(models.Model):
    employee = models.ForeignKey(CV, on_delete=models.CASCADE)
    id_card = models.BooleanField(default=False)
    laptop = models.BooleanField(default=False)

class AdminProvision(models.Model):
    employee = models.ForeignKey(CV, on_delete=models.CASCADE)
    bank_account_paper = models.BooleanField(default=False)
    sim_card = models.BooleanField(default=False)
    visiting_card = models.BooleanField(default=False)
    placement = models.BooleanField(default=False)

class FinanceProvision(models.Model):
    employee = models.ForeignKey(CV, on_delete=models.CASCADE)
    payroll_notification_sent = models.BooleanField(default=False)
    payroll_pdf = models.FileField(upload_to="payrolls/", blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    sent_payroll_pdf = models.BooleanField(default=False)

    def __str__(self):
        return f"Finance Provision for {self.employee.name}"

# Signal to send email on CV submission
@receiver(post_save, sender=CV)
def send_cv_submission_email(sender, instance, created, **kwargs):
    if created:
        subject = "CV Submission Confirmation"
        message = f"Dear {instance.name},\n\nThank you for submitting your CV. We will review it and get back to you soon."
        
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[instance.email],
            fail_silently=True
        )

        # Log Email
        EmailLog.objects.create(
            recipient=instance.email,
            subject=subject,
            message=message
        )

# Signal to send email when EmployeeDocument is marked as sent
@receiver(post_save, sender=EmployeeDocument)
def send_employee_document_email(sender, instance, **kwargs):
    if instance.sent_to_email:
        subject = "Your Document from TAD Group"
        message = f"Dear {instance.employee.name},\n\nYour {instance.get_document_type_display()} has been sent to you. Please find the document attached."

        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[instance.employee.email],
            fail_silently=True
        )

        # Log Email
        EmailLog.objects.create(
            recipient=instance.employee.email,
            subject=subject,
            message=message
        )


@receiver(post_save, sender=FinanceProvision)
def send_payroll_email(sender, instance, **kwargs):
    if instance.sent_payroll_pdf and instance.payroll_pdf and instance.email:
        subject = "Your Payroll Document"
        message = f"Dear {instance.employee.name},\n\nPlease find attached your payroll document."
        
        email = EmailMessage(
            subject=subject,
            body=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[instance.email],
        )
        email.attach_file(instance.payroll_pdf.path)
        email.send(fail_silently=True)
        # Log Email
        EmailLog.objects.create(
            recipient=instance.email,
            subject=subject,
            message=message
        )        