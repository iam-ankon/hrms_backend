from rest_framework import viewsets, permissions
from knox.models import AuthToken
from rest_framework.response import Response
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from .models import EmployeeProfile, Attendance, LeaveRequest, Payroll
from .serializers import EmployeeProfileSerializer, AttendanceSerializer, LeaveRequestSerializer, PayrollSerializer, UserSerializer

class EmployeeProfileViewSet(viewsets.ModelViewSet):
    queryset = EmployeeProfile.objects.all()
    serializer_class = EmployeeProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [permissions.IsAuthenticated]

class LeaveRequestViewSet(viewsets.ModelViewSet):
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

class PayrollViewSet(viewsets.ModelViewSet):
    queryset = Payroll.objects.all()
    serializer_class = PayrollSerializer
    permission_classes = [permissions.IsAuthenticated]

class LoginView(viewsets.ViewSet):
    def create(self, request):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response({
            "user": UserSerializer(user).data,
            "token": AuthToken.objects.create(user)[1]
        })
