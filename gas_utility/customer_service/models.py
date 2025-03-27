from django.db import models
from django.core.validators import FileExtensionValidator

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, db_index=True) 
    phone = models.CharField(max_length=15, unique=True, db_index=True)
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
    
    REQUEST_TYPES = [
        ('leak', 'Gas Leak'),
        ('billing', 'Billing Inquiry'),
        ('new', 'New Connection'),
        ('other', 'Other'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="service_requests")
    request_type = models.CharField(max_length=20, choices=REQUEST_TYPES, default='other') 
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

    attachment = models.FileField(
        upload_to='attachments/', 
        null=True, 
        blank=True,
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'png', 'jpeg', 'docx'])]
    )

    def __str__(self):
        return f"Request {self.id} - {self.get_request_type_display()} ({self.status})" 

    def get_attachment_url(self):
        """Returns the URL of the uploaded attachment."""
        if self.attachment:
            return self.attachment.url
        return None

class CustomerSupportRepresentative(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, db_index=True)
    phone = models.CharField(max_length=15, unique=True, db_index=True)
    assigned_requests = models.ManyToManyField(ServiceRequest, blank=True, related_name="assigned_representatives")
    role = models.CharField(max_length=50, default="Support Agent")

    def __str__(self):
        return self.name