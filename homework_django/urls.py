from django.contrib import admin
from django.urls import path

import ads.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ads.views.index),
    path('cat/', ads.views.CategoryView.as_view()),
    path('ads/', ads.views.AdsView.as_view()),
    path('ads/<int:pk>/', ads.views.AdDetailView.as_view()),
    path('cat/<int:pk>/', ads.views.CategoryDetailView.as_view()),
]
