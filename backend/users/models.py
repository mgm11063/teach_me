from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    phone_number = models.CharField(
        max_length=15,
        unique=True,
        validators=[
            RegexValidator(
                regex=r"^01[016789]-\d{3,4}-\d{4}$",
                message="휴대폰 번호 형식이 올바르지 않습니다. (예: 010-1234-5678)",
            ),
        ],
        help_text="휴대폰 번호를 입력하세요. (예: 010-1234-5678)",
    )
