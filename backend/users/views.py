from .serializers import UserSerializer
from .models import User
from rest_framework.generics import RetrieveAPIView,CreateAPIView

class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
