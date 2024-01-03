from .models import Question, QuestionMedia
from rest_framework import serializers
from categories.serializers import CategorySerializer
from answers.serializers import AnswerSerializer


class QuestionMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionMedia
        fields = ["file"]


class QuestionSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    user = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ["title", "content", "reward", "user", "categories"]

    def get_user(self, obj):
        from users.serializers import UserProfileSerializer  # lazy import

        serializer = UserProfileSerializer(obj.user)
        return serializer.data


class QuestionDetailSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)
    categories = CategorySerializer(many=True, read_only=True)
    media = QuestionMediaSerializer(many=True, read_only=True)
    user = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = [
            "media",
            "title",
            "content",
            "reward",
            "user",
            "categories",
            "answers",
        ]

    def get_user(self, obj):
        from users.serializers import UserProfileSerializer  # lazy import

        serializer = UserProfileSerializer(obj.user)
        return serializer.data
