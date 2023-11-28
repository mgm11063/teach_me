from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")
        Other = ("other", "Other")

    name = models.CharField(
        max_length=150,
        default="",
    )
    avatar = models.URLField(blank=True)
    gender = models.CharField(
        max_length=10,
        choices=GenderChoices.choices,
    )
