from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from customer_service import views  # Import views from customer_service

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    # Customer Service App URLs
    path('customer_service/', include('customer_service.urls')),

    # Home Page
    path('', views.home, name='home'),

    path('customer_service/', include('customer_service.urls')),  # Include app routes

]

# Serving media & static files in development mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
