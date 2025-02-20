from django.contrib import admin
from .models import Employee, Attendance, Leave, Payroll, PerformanceReview, Training, Compliance

admin.site.register(Employee)
admin.site.register(Attendance)
admin.site.register(Leave)
admin.site.register(Payroll)
admin.site.register(PerformanceReview)
admin.site.register(Training)
admin.site.register(Compliance)
