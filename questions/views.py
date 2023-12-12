
from .models import Question
from .serializers import QuestionSerializer,QuestionDetailSerializer
from .services import handle_uploaded_files
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.generics import RetrieveAPIView
from django_filters.rest_framework import DjangoFilterBackend


class QuestionListView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ["title", "content"]

    def get(self, request):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QuestionDetailView(RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionDetailSerializer

class QuestionMediaUploadView(APIView):
    def post(self, request, question_id):
        question = get_object_or_404(Question, pk=question_id)

        if len(request.FILES) > 5:
            return Response({"error": "최대 5개의 파일만 업로드할 수 있습니다."}, status=status.HTTP_400_BAD_REQUEST)

        response = handle_uploaded_files(question, request.FILES.values())
        if "error" in response:
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

        return Response(response, status=status.HTTP_201_CREATED)

 
 