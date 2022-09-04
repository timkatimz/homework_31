from django.urls import path

import category.views

urlpatterns = [
    path('', category.views.CategoryListView.as_view()),
    path('<int:pk>/', category.views.CategoryDetailView.as_view()),
    path('create/', category.views.CategoryCreateView.as_view()),
    path('update/<int:pk>/', category.views.CategoryUpdateView.as_view()),
    path('delete/<int:pk>/', category.views.CategoryDeleteView.as_view()),
    ]
