from django.contrib import admin
from django.urls import path, include

import ads.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ads/', include("ads.urls")),
    path('cat/', include("category.urls")),
    path('user/', include("users.urls")),
]
