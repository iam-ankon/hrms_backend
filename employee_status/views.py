from rest_framework import viewsets
from .models import Employee, Attendance, Leave, Payroll, PerformanceReview, Training, Compliance
from .serializers import EmployeeSerializer, AttendanceSerializer, LeaveSerializer, PayrollSerializer, PerformanceReviewSerializer, TrainingSerializer, ComplianceSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

class LeaveViewSet(viewsets.ModelViewSet):
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer

class PayrollViewSet(viewsets.ModelViewSet):
    queryset = Payroll.objects.all()
    serializer_class = PayrollSerializer

class PerformanceReviewViewSet(viewsets.ModelViewSet):
    queryset = PerformanceReview.objects.all()
    serializer_class = PerformanceReviewSerializer

class TrainingViewSet(viewsets.ModelViewSet):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer

class ComplianceViewSet(viewsets.ModelViewSet):
    queryset = Compliance.objects.all()
    serializer_class = ComplianceSerializer
