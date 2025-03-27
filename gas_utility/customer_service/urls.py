from django.urls import path
from customer_service.views import upload_attachment
from .views import (
    home,
    get_request_details,
    list_service_requests,
    create_service_request,
    ServiceRequestListCreateView,
    ServiceRequestDetailView,
    customer_account_info
)

urlpatterns = [
    path('api/service-requests/', create_service_request, name='create-request'),
    
    path('api/service-requests/upload/', upload_attachment, name='upload-attachment'),
    
    path('api/service-requests/<int:pk>/', ServiceRequestDetailView.as_view(), name='request-detail'),

    path('api/account/', customer_account_info, name='customer-account-info'),
    
    path('', home, name='home')
]