from django.db import models
from core.models import CoreModel
from users.models import User
from questions.models import Question


class Answer(CoreModel):
    content = models.TextField(max_length=999)
    user = models.ForeignKey(User,related_name='answers', on_delete=models.CASCADE)
    question = models.ForeignKey(
        Question, related_name="answers", on_delete=models.CASCADE
    )
    is_accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.question.title
