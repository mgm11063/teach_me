from django.urls import path
from . import views

urlpatterns = [
    path("<int:question_id>", views.AcceptAnswerView.as_view()),
]
