from django.db import models
from core.models import CoreModel
from users.models import User
from categories.models import Category


class Question(CoreModel):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=999)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title
