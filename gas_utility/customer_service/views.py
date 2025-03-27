from django.utils.timezone import now
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import ServiceRequest, Customer
from .serializers import ServiceRequestSerializer
from rest_framework import generics
from django.http import JsonResponse
from django.shortcuts import render

def home(request):
    return JsonResponse({
        "message": "Welcome to Bynry Inc. Customer Service!",
        "status": "active",
        "endpoints": {
            "create_request": "/api/service-requests/",
            "list_requests": "/requests/"
        },
        "account_info": "/api/account/?customer_id=<ID>",
    })

@api_view(['POST'])
def create_service_request(request):
    try:
        required_fields = ['name', 'phone', 'request_type', 'description']
        missing = [f for f in required_fields if not request.data.get(f)]
        if missing:
            return Response({"error": f"Missing fields: {', '.join(missing)}"}, status=400)

        customer = Customer.objects.create(
            name=request.data['name'],
            phone=request.data['phone'],
            address=request.data.get('address', '')
        )
        
        service_request = ServiceRequest.objects.create(
            customer=customer,
            request_type=request.data['request_type'],
            description=request.data['description']
        )

        return Response({
            "request_id": service_request.id,
            "customer_id": customer.id,
            "message": "Service request created. Use customer_id to upload files."
        }, status=201)

    except Exception as e:
        return Response({"error": str(e)}, status=400)

@api_view(['POST'])
def upload_attachment(request):
    try:
        if 'customer' not in request.data or 'attachment' not in request.data:
            return Response({"error": "customer and attachment are required"}, status=400)

        customer = Customer.objects.get(id=request.data['customer'])
        service_request = ServiceRequest.objects.filter(customer=customer).last()
        
        if not service_request:
            return Response({"error": "No service request found for this customer"}, status=404)

        service_request.attachment = request.data['attachment']
        service_request.save()

        return Response({
            "request_id": service_request.id,
            "attachment_url": service_request.attachment.url
        }, status=200)

    except Customer.DoesNotExist:
        return Response({"error": "Customer not found"}, status=404)


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
    requests = ServiceRequest.objects.all()
    serializer = ServiceRequestSerializer(requests, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def customer_account_info(request):
    customer_id = request.GET.get('customer_id')  
    try:
        customer = Customer.objects.get(id=customer_id)
        return JsonResponse({
            "name": customer.name,
            "email": customer.email,
            "phone": customer.phone,
            "address": customer.address,
            "active_requests": customer.service_requests.filter(status__in=['pending', 'in_progress']).count()
        })
    except Customer.DoesNotExist:
        return JsonResponse({"error": "Customer not found"}, status=404)
        
@api_view(['GET'])
def service_types(request):
    return Response({
        "service_types": dict(ServiceRequest.REQUEST_TYPES),
        "message": "Use these exact values when submitting requests"
    })
    
class ServiceRequestListCreateView(generics.ListCreateAPIView):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer
    parser_classes = (MultiPartParser, FormParser)

class ServiceRequestDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer

class ServiceRequestCreateView(APIView):
    parser_classes = (MultiPartParser, FormParser)  

    def post(self, request, *args, **kwargs):
        serializer = ServiceRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ServiceRequestViewSet(viewsets.ModelViewSet):
    queryset = ServiceRequest.objects.all()
    serializer_class = ServiceRequestSerializer
    parser_classes = (MultiPartParser, FormParser)


