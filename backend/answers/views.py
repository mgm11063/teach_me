from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Question, Answer
from .serializers import AnswerSerializer
from .services import select_answer_and_award_reward


class AcceptAnswerView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, question_id):
        try:
            question = Question.objects.get(id=question_id)
            answers = Answer.objects.filter(question=question)

            serializer = AnswerSerializer(answers, many=True)
            return Response(serializer.data)

        except Question.DoesNotExist:
            return Response(
                {"error": "질문이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND
            )

    def post(self, request, question_id, answer_id):
        user = request.user

        try:
            question = Question.objects.get(id=question_id)
            if user != question.user:
                return Response(
                    {"error": "권한이 없습니다."}, status=status.HTTP_403_FORBIDDEN
                )

            select_answer_and_award_reward(question_id, answer_id)
            return Response({"message": "답변이 선택되었습니다."}, status=status.HTTP_200_OK)

        except Question.DoesNotExist:
            return Response(
                {"error": "질문이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND
            )
        except Answer.DoesNotExist:
            return Response(
                {"error": "답변이 존재하지 않습니다."}, status=status.HTTP_404_NOT_FOUND
            )
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
