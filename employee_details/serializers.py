from rest_framework import serializers
from .models import EmployeeDetails, EmergencyContact, Notification, EmailLog

class EmergencyContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmergencyContact
        fields = '__all__'

class EmployeeDetailsSerializer(serializers.ModelSerializer):
    emergency_contact = EmergencyContactSerializer()

    class Meta:
        model = EmployeeDetails
        fields = '__all__'

    def create(self, validated_data):
        emergency_contact_data = validated_data.pop('emergency_contact')
        emergency_contact = EmergencyContact.objects.create(**emergency_contact_data)
        employee = EmployeeDetails.objects.create(emergency_contact=emergency_contact, **validated_data)
        return employee

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

# Email Log Serializer
class EmailLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailLog
        fields = '__all__'
