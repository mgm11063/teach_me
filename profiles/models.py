from django.db import models
from core.models import CoreModel
from users.models import User


class Profile(CoreModel):
    class GenderChoices(models.TextChoices):
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")
        Other = ("other", "Other")

    name = models.CharField(
        max_length=150,
        default="",
    )
    user = models.ForeignKey(User, related_name="profiles", on_delete=models.CASCADE)
    avatar = models.URLField(blank=True)
    gender = models.CharField(
        max_length=10,
        choices=GenderChoices.choices,
    )
    bio = models.TextField(max_length=500)
    reward_points = models.IntegerField(default=0)

    def __str__(self):
        return self.name
