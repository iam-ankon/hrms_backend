from django.contrib import admin
from .models import *

admin.site.register(Department)
admin.site.register(CV)
admin.site.register(RequirementAnalysis)
admin.site.register(Interview)
admin.site.register(EmployeeDocument)
admin.site.register(ITProvision)
admin.site.register(AdminProvision)

admin.site.register(CVAdd)
admin.site.register(CategorizedCV)

@admin.register(EmailLog)
class EmailLogAdmin(admin.ModelAdmin):
    list_display = ('recipient', 'subject', 'sent_at')
    search_fields = ('recipient', 'subject')
    list_filter = ('sent_at',)


@admin.register(FinanceProvision)
class FinanceProvisionAdmin(admin.ModelAdmin):
    list_display = ('employee', 'payroll_notification_sent', 'sent_payroll_pdf', 'email')
    list_filter = ('sent_payroll_pdf',)
    search_fields = ('employee__name', 'email')
