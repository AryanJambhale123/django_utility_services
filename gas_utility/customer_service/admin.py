from django.contrib import admin
from .models import Customer, ServiceRequest, CustomerSupportRepresentative

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address')
    search_fields = ('name', 'email')

@admin.register(ServiceRequest)  
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'request_type', 'status', 'created_at')
    list_filter = ('request_type', 'status')  
    raw_id_fields = ('customer',) 

@admin.register(CustomerSupportRepresentative)
class RepresentativeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'role')
