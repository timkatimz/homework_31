from django.urls import path

import users.views

urlpatterns = [
    path('', users.views.UserListView.as_view()),
    path('<int:pk>/', users.views.UserDetailView.as_view()),
    ]
