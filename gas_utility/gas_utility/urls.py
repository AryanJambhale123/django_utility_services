from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from customer_service import views  
from django.contrib import admin
from customer_service.views import home  

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/', include('customer_service.urls')), 

    path('', include('customer_service.urls')),
    
    path('', home, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
