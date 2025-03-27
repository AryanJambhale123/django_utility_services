from rest_framework import serializers
from .models import ServiceRequest 

class ServiceRequestSerializer(serializers.ModelSerializer):
    attachment = serializers.FileField(required=False)

    class Meta:
        model = ServiceRequest
        fields = '__all__'
    def validate_request_type(self, value):
        valid_types = [choice[0] for choice in ServiceRequest.REQUEST_TYPES]
        if value not in valid_types:
            raise serializers.ValidationError(
                f"Invalid request type. Valid options are: {', '.join(valid_types)}"
            )
        return value