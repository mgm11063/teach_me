from django.db import models
from core.models import CoreModel
from users.models import User
from categories.models import Category


class Question(CoreModel):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=999)
    user = models.ForeignKey(User, related_name="questions", on_delete=models.CASCADE)
    reward = models.PositiveIntegerField(default=0)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title


class QuestionMedia(CoreModel):
    question = models.ForeignKey(
        Question, related_name="media", on_delete=models.CASCADE
    )
    file = models.FileField(upload_to="questions/media/")
