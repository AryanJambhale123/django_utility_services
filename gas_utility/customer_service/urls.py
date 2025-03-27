from django.urls import path
from .views import home, update_service_request_status, get_request_details, list_service_requests, create_service_request,ServiceRequestListCreateView,ServiceRequestDetailView

urlpatterns = [
    path("", home, name="home"),
    path("request/<int:pk>/", get_request_details, name="get_request"),
    path("request/<int:pk>/update/", update_service_request_status, name="update_request"),
    path("requests/", list_service_requests, name="list_requests"),
    path("request/create/", create_service_request, name="create_service_request"),
    path('api/service-requests/', ServiceRequestListCreateView.as_view(), name='service-request-list-create'),
    path('api/service-requests/<int:pk>/', ServiceRequestDetailView.as_view(), name='service-request-detail'),
]
