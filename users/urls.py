from django.urls import path
from .views import UserListView, UserDetailView, login

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('login/', login, name='login'),
] 