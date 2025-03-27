from rest_framework import serializers
from .models import ServiceRequest  # Import your model

class ServiceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceRequest
        fields = ['customer', 'description', 'status']
