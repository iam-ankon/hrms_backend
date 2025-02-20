from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register("departments", DepartmentViewSet)
router.register("cvs", CVViewSet)
router.register("requirements", RequirementAnalysisViewSet)
router.register("interviews", InterviewViewSet)
router.register("documents", EmployeeDocumentViewSet)
router.register("it_provisions", ITProvisionViewSet)
router.register("admin_provisions", AdminProvisionViewSet)
router.register("finance_provisions", FinanceProvisionViewSet)
router.register("email_logs", EmailLogViewSet) 
router.register("CVAdd", CVAddViewSet) 
router.register('categorized_cvs', CategorizedCVViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
