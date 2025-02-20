from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, AttendanceViewSet, LeaveViewSet, PayrollViewSet, PerformanceReviewViewSet, TrainingViewSet, ComplianceViewSet

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)
router.register(r'attendance', AttendanceViewSet)
router.register(r'leave', LeaveViewSet)
router.register(r'payroll', PayrollViewSet)
router.register(r'performance', PerformanceReviewViewSet)
router.register(r'training', TrainingViewSet)
router.register(r'compliance', ComplianceViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
