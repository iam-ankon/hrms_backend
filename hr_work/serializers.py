from rest_framework import serializers
from .models import *

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"

class CVSerializer(serializers.ModelSerializer):
    class Meta:
        model = CV
        fields = "__all__"

class RequirementAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequirementAnalysis
        fields = "__all__"

class InterviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interview
        fields = "__all__"

class EmployeeDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeDocument
        fields = "__all__"

class ITProvisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ITProvision
        fields = "__all__"

class AdminProvisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminProvision
        fields = "__all__"

class FinanceProvisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinanceProvision
        fields = '__all__'

class EmailLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailLog
        fields = '__all__'


class CVAddSerializer(serializers.ModelSerializer):
    class Meta:
        model = CVAdd
        fields = '__all__'


class CategorizedCVSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategorizedCV
        fields = '__all__'