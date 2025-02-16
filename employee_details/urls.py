from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeDetailsViewSet, EmergencyContactViewSet, NotificationViewSet, EmailLogViewSet

router = DefaultRouter()
router.register('employees', EmployeeDetailsViewSet)
router.register('emergency_contacts', EmergencyContactViewSet)
router.register('notifications', NotificationViewSet)
router.register('email_logs', EmailLogViewSet)  # New Email Log API

urlpatterns = [
    path('api/', include(router.urls)),
]
