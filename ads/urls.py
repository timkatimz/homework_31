from django.urls import path

import ads.views

urlpatterns = [
    path('', ads.views.AdsListView.as_view()),
    path('<int:pk>/', ads.views.AdsDetailView.as_view()),
    path('create/', ads.views.AdsCreateView.as_view()),
    path('<int:pk>/update/', ads.views.AdsUpdateView.as_view()),
    path('<int:pk>/delete/', ads.views.AdsDeleteView.as_view()),
]
