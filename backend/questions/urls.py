from . import views
from .views import QuestionMediaUploadView
from django.urls import path

urlpatterns = [
    path("", views.QuestionListView.as_view()),
    path("<int:pk>", views.QuestionDetailView.as_view()),
    path('<int:question_id>/media/', QuestionMediaUploadView.as_view(), name='question-media-upload'),
]
