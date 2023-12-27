from . import views
from .views import ProfileDetailView
from django.urls import path

urlpatterns = [
    path("<int:pk>", views.ProfileDetailView.as_view()),
]
