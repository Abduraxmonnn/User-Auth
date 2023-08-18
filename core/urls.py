from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as swagger_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.user.urls'))
]

urlpatterns += swagger_urls
