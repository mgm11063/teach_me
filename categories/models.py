from django.db import models
from core.models import CoreModel


class Category(CoreModel):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
