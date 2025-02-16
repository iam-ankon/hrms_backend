from io import BytesIO
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework import viewsets, permissions
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from .models import EmployeeDetails, EmergencyContact, Notification, EmailLog
from .serializers import EmployeeDetailsSerializer, EmergencyContactSerializer, NotificationSerializer, EmailLogSerializer
from rest_framework import viewsets, permissions

# Employee ViewSet
class EmployeeDetailsViewSet(viewsets.ModelViewSet):
    queryset = EmployeeDetails.objects.all()
    serializer_class = EmployeeDetailsSerializer
    permission_classes = [permissions.IsAuthenticated]

# Emergency Contact ViewSet
class EmergencyContactViewSet(viewsets.ModelViewSet):
    queryset = EmergencyContact.objects.all()
    serializer_class = EmergencyContactSerializer
    permission_classes = [permissions.IsAuthenticated]

# Notifications ViewSet
class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

class EmailLogViewSet(viewsets.ModelViewSet):
    queryset = EmailLog.objects.all()
    serializer_class = EmailLogSerializer
    permission_classes = [permissions.IsAuthenticated]

# Print Employee Details as PDF
@api_view(['GET'])
def print_employee_details(request, employee_id):
    employee = EmployeeDetails.objects.get(employee_id=employee_id)

    # Render HTML template
    html = render_to_string('employee_details_print_template.html', {'employee_details': employee})

    # Create the response as a PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{employee.name}_details.pdf"'

    # Convert HTML to PDF
    pisa_status = pisa.CreatePDF(BytesIO(html.encode('UTF-8')), dest=response)

    if pisa_status.err:
        return HttpResponse('Error generating PDF', status=500)

    return response
