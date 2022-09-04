from django.urls import path

import ads.views

urlpatterns = [
    path('', ads.views.AdsListView.as_view()),
    path('<int:pk>/', ads.views.AdsDetailView.as_view()),
    path('create/', ads.views.AdsCreateView.as_view()),
    path('update/<int:pk>/', ads.views.AdsUpdateView.as_view()),
    path('delete/<int:pk>/', ads.views.AdsDeleteView.as_view()),
    path('upload_image/<int:pk>/', ads.views.AdsUploadImageView.as_view()),
]
