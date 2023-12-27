from django.db import models
from core.models import CoreModel
from users.models import User


class Profile(CoreModel):
    class GenderChoices(models.TextChoices):
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")
        Other = ("other", "Other")

    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    avatar = models.URLField(blank=True)
    gender = models.CharField(
        max_length=10,
        choices=GenderChoices.choices,
    )
    bio = models.TextField(max_length=500, blank=True)
    reward_points = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.user.username}'s profile"
