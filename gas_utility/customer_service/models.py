from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, db_index=True)  # Indexed for faster lookups
    phone = models.CharField(max_length=15, unique=True, db_index=True)  # Indexed for performance
    address = models.TextField()

    def __str__(self):
        return self.name

class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="service_requests")
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', db_index=True)  # Indexed for efficiency
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    resolved_at = models.DateTimeField(null=True, blank=True)
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)

    def __str__(self):
        return f"Request {self.id} - {self.status}"

class CustomerSupportRepresentative(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, db_index=True)  # Indexed for performance
    phone = models.CharField(max_length=15, unique=True, db_index=True)  # Indexed for performance
    assigned_requests = models.ManyToManyField(ServiceRequest, blank=True, related_name="assigned_representatives")

    def __str__(self):
        return self.name
