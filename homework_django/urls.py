from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from users.views import LocationsViewSet

location_router = routers.SimpleRouter()
location_router.register(r'location', LocationsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ads/', include("ads.urls")),
    path('cat/', include("category.urls")),
    path('user/', include("users.urls")),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += location_router.urls