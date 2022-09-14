from django.urls import path

import selection.views

urlpatterns = [
    path('', selection.views.SelectionListView.as_view()),
    path('<int:pk>/', selection.views.SelectionDetailView.as_view()),
    path('create/', selection.views.SelectionCreateView.as_view()),
    path('update/<int:pk>/', selection.views.SelectionUpdateView.as_view()),
    path('delete/<int:pk>/', selection.views.SelectionDeleteView.as_view()),
    ]
