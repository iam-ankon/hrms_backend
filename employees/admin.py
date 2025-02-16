from django.contrib import admin
from .models import CustomUser, EmployeeProfile, Attendance, LeaveRequest, Payroll

# Register Custom User model
admin.site.register(CustomUser)

# Register Employee Profile model
class EmployeeProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'position', 'department', 'salary', 'date_joined')
    search_fields = ('user__username', 'position', 'department')

admin.site.register(EmployeeProfile, EmployeeProfileAdmin)

# Register Attendance model
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date', 'status')
    search_fields = ('employee__username', 'status')
    list_filter = ('status',)

admin.site.register(Attendance, AttendanceAdmin)

# Register Leave Request model
class LeaveRequestAdmin(admin.ModelAdmin):
    list_display = ('employee', 'start_date', 'end_date', 'status')
    search_fields = ('employee__username', 'status')
    list_filter = ('status',)

admin.site.register(LeaveRequest, LeaveRequestAdmin)

# Register Payroll model
class PayrollAdmin(admin.ModelAdmin):
    list_display = ('employee', 'month', 'salary_paid', 'payment_date')
    search_fields = ('employee__username', 'month')

admin.site.register(Payroll, PayrollAdmin)
