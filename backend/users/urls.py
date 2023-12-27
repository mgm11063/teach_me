from .views import UserCreateView, UserDetailView, UserProfileView
from django.urls import path

urlpatterns = [
    path("", UserCreateView.as_view()),
    path("<int:pk>", UserDetailView.as_view()),
    path("<int:pk>/profile", UserProfileView.as_view(), name="user-profile"),
]
