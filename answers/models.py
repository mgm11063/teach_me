from django.db import models
from core.models import CoreModel
from users.models import User
from questions.models import Question


class Answer(CoreModel):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return f"Answer to {self.question.title}"
