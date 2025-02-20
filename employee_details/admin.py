from django.urls import path
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.urls import reverse
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from .models import EmployeeDetails, EmergencyContact, Notification, EmailLog


class EmployeeDetailsAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'name', 'designation', 'department', 'salary', 'attendance_delay')
    search_fields = ('name', 'designation', 'department')
    list_filter = ('attendance_delay', 'department')

    actions = ['preview_employee_details']

    def preview_employee_details(self, request, queryset):
        """ Redirect to the preview page before printing """
        if queryset.count() != 1:
            self.message_user(request, "Please select only one employee for preview.", level="error")
            return redirect(request.get_full_path())

        employee = queryset.first()
        return redirect(reverse('admin:employee_details_preview', args=[employee.id]))

    preview_employee_details.short_description = "Preview selected employee details"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('employee-preview/<int:employee_id>/', self.admin_site.admin_view(self.employee_preview), name="employee_details_preview"),
            path('employee-print/<int:employee_id>/', self.admin_site.admin_view(self.generate_employee_pdf), name="employee_details_print"),
        ]
        return custom_urls + urls

    def employee_preview(self, request, employee_id):
        """ Render the preview page before printing """
        employee = EmployeeDetails.objects.get(id=employee_id)
        return render(request, 'admin/employee_preview.html', {'employee': employee})

    def generate_employee_pdf(self, request, employee_id):
        """ Generate PDF after previewing """
        employee = EmployeeDetails.objects.get(id=employee_id)

        buffer = BytesIO()
        c = canvas.Canvas(buffer, pagesize=letter)
        width, height = letter

        c.setFont("Helvetica", 12)
        c.drawString(100, height - 100, f"Employee ID: {employee.employee_id}")
        c.drawString(100, height - 120, f"Name: {employee.name}")
        c.drawString(100, height - 140, f"Designation: {employee.designation}")
        c.drawString(100, height - 160, f"Department: {employee.department}")
        c.drawString(100, height - 180, f"Salary: {employee.salary}")
        c.drawString(100, height - 200, f"Attendance Delay: {'Yes' if employee.attendance_delay else 'No'}")
        c.drawString(100, height - 220, f"Email: {employee.email}")
        c.drawString(100, height - 240, f"Phone: {employee.personal_phone}")

        c.showPage()
        c.save()

        pdf = buffer.getvalue()
        buffer.close()

        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="employee_{employee.employee_id}_details.pdf"'

        return response


admin.site.register(EmployeeDetails, EmployeeDetailsAdmin)
admin.site.register(EmergencyContact)
admin.site.register(Notification)


@admin.register(EmailLog)
class EmailLogAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'subject', 'sent_at')
    search_fields = ('recipient', 'subject')
    list_filter = ('sent_at',)
