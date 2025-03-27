from django.contrib import admin
from .models import Customer, ServiceRequest, CustomerSupportRepresentative

admin.site.register(Customer)
admin.site.register(ServiceRequest)
admin.site.register(CustomerSupportRepresentative)

# Register your models here.
