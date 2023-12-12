from .views import UserCreateView,UserDetailView
from django.urls import path

urlpatterns = [
    path("", UserCreateView.as_view()),
    path("<int:pk>", UserDetailView.as_view()),
]
