from rest_framework import serializers
from .models import Question
from categories.serializers import CategorySerializer
from answers.serializers import AnswerSerializer


class QuestionSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ["title", "content", "reward", "user", "categories"]


class QuestionDetailSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ["title", "content", "reward", "user", "categories", "answers"]
