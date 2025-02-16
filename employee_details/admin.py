from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib import admin
from .models import EmployeeDetails, EmergencyContact, Notification, EmailLog
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO


class EmployeeDetailsAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'name', 'designation', 'department', 'salary', 'attendance_delay')
    search_fields = ('name', 'designation', 'department')
    list_filter = ('attendance_delay', 'department')

    actions = ['print_employee_details']

    def print_employee_details(self, request, queryset):
        # Prepare the PDF content
        employee = queryset.first()
        
        # Create an in-memory buffer for the PDF
        buffer = BytesIO()
        
        # Create a canvas to draw on the PDF
        c = canvas.Canvas(buffer, pagesize=letter)
        width, height = letter

        # Add employee details to the PDF
        c.setFont("Helvetica", 12)
        c.drawString(100, height - 100, f"Employee ID: {employee.employee_id}")
        c.drawString(100, height - 120, f"Name: {employee.name}")
        c.drawString(100, height - 140, f"Designation: {employee.designation}")
        c.drawString(100, height - 160, f"Department: {employee.department}")
        c.drawString(100, height - 180, f"Salary: {employee.salary}")
        c.drawString(100, height - 200, f"Attendance Delay: {'Yes' if employee.attendance_delay else 'No'}")

        # If you have other details to display, add them in a similar manner
        c.drawString(100, height - 220, f"Email: {employee.email}")
        c.drawString(100, height - 240, f"Phone: {employee.personal_phone}")

        # You can add more employee fields here as required

        # Finalize the PDF
        c.showPage()
        c.save()

        # Get the PDF content from the buffer
        pdf = buffer.getvalue()
        buffer.close()

        # Create a response with PDF content
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="employee_{employee.employee_id}_details.pdf"'

        return response

    print_employee_details.short_description = "Print selected employee details"

admin.site.register(EmployeeDetails, EmployeeDetailsAdmin)
admin.site.register(EmergencyContact)
admin.site.register(Notification)


# Register Email Log Model
@admin.register(EmailLog)
class EmailLogAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'subject', 'sent_at')
    search_fields = ('recipient', 'subject')
    list_filter = ('sent_at',)