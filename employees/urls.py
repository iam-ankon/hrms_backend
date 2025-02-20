from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from employees.views import EmployeeProfileViewSet, AttendanceViewSet, LeaveRequestViewSet, PayrollViewSet, LoginView

router = DefaultRouter()
router.register('employees', EmployeeProfileViewSet)
router.register('attendance', AttendanceViewSet)
router.register('leave', LeaveRequestViewSet)
router.register('payroll', PayrollViewSet)

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # path('api/login/', LoginView.as_view({'post': 'create'})),
]
