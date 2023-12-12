from .models import Question,QuestionMedia
from django.contrib import admin


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass


@admin.register(QuestionMedia)
class QuestionMediaAdmin(admin.ModelAdmin):
    pass

