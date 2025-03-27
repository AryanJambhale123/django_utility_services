from django.utils.timezone import now
from django.views.decorators.csrf import csrf_exempt  # Optional: Remove in production
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import ServiceRequest, Customer
from .serializers import ServiceRequestSerializer
from rest_framework import generics


def home(request):
    return JsonResponse({"message": "Welcome to Customer Service!"})

@api_view(['POST'])
def create_service_request(request):
    try:
        customer_id = request.data.get('customer')  # Ensure it uses 'customer' key
        description = request.data.get('description')

        if not customer_id or not description:
            return Response({"error": "customer and description are required fields"}, status=status.HTTP_400_BAD_REQUEST)

        customer = Customer.objects.get(id=customer_id)  # Fetch customer instance
        service_request = ServiceRequest.objects.create(customer=customer, description=description)

        serializer = ServiceRequestSerializer(service_request)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    except Customer.DoesNotExist:
        return Response({"error": "Customer not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(["POST"])
def update_service_request_status(request, pk):
    service_request = get_object_or_404(ServiceRequest, pk=pk)

    new_status = request.data.get("status")
    if not new_status:
        return Response({"error": "Status field is required"}, status=status.HTTP_400_BAD_REQUEST)

    service_request.status = new_status
    service_request.updated_at = now()  
    service_request.save()

    return Response({"message": "Status updated successfully"}, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_request_details(request, pk):
    service_request = get_object_or_404(ServiceRequest, pk=pk)
    return Response({
        "request_id": service_request.id,
        "status": service_request.status,
        "created_at": service_request.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        "updated_at": service_request.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
        "resolved_at": service_request.resolved_at.strftime("%Y-%m-%d %H:%M:%S") if service_request.resolved_at else None
    })


@api_view(["GET"])
def list_service_requests(request):
    requests = ServiceRequest.objects.all().values(
        "id", "status", "created_at", "updated_at", "resolved_at"
    )
    return Response(list(requests))

class ServiceRequestListCreateView(generics.ListCreateAPIView):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer

class ServiceRequestDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer