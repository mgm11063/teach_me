from .models import User
from answers.serializers import AnswerSerializer
from questions.serializers import QuestionSerializer
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)
    questions = QuestionSerializer(many=True,read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username','phone_number' ,'email', 'first_name', 'last_name','answers','questions']
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
