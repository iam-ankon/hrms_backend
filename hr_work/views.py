from .models import *
from .serializers import *
from rest_framework import viewsets
from .models import EmployeeDocument, EmailLog, CVAdd, CategorizedCV, ITProvision, AdminProvision, FinanceProvision, Department, RequirementAnalysis, Interview
from .serializers import CVSerializer, EmployeeDocumentSerializer, EmailLogSerializer, CVAddSerializer, CategorizedCVSerializer, ITProvisionSerializer, AdminProvisionSerializer, FinanceProvisionSerializer, DepartmentSerializer, RequirementAnalysisSerializer, InterviewSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class CVViewSet(viewsets.ModelViewSet):
    queryset = CV.objects.all()
    serializer_class = CVSerializer

class RequirementAnalysisViewSet(viewsets.ModelViewSet):
    queryset = RequirementAnalysis.objects.all()
    serializer_class = RequirementAnalysisSerializer

class InterviewViewSet(viewsets.ModelViewSet):
    queryset = Interview.objects.all()
    serializer_class = InterviewSerializer



class CVAddViewSet(viewsets.ModelViewSet):
    queryset = CVAdd.objects.all()
    serializer_class = CVAddSerializer

class CategorizedCVViewSet(viewsets.ModelViewSet):
    queryset = CategorizedCV.objects.all()
    serializer_class = CategorizedCVSerializer
        

class ITProvisionViewSet(viewsets.ModelViewSet):
    queryset = ITProvision.objects.all()
    serializer_class = ITProvisionSerializer

class AdminProvisionViewSet(viewsets.ModelViewSet):
    queryset = AdminProvision.objects.all()
    serializer_class = AdminProvisionSerializer

class FinanceProvisionViewSet(viewsets.ModelViewSet):
    queryset = FinanceProvision.objects.all()
    serializer_class = FinanceProvisionSerializer


class EmailLogViewSet(viewsets.ModelViewSet):
    queryset = EmailLog.objects.all()
    serializer_class = EmailLogSerializer

    def get_queryset(self):
        return EmailLog.objects.filter(
            recipient__in=EmployeeDocument.objects.filter(sent_to_email=True).values_list('employee__email', flat=True)
        )
    

class EmployeeDocumentViewSet(viewsets.ModelViewSet):
    queryset = EmployeeDocument.objects.all()
    serializer_class = EmployeeDocumentSerializer




