from rest_framework import generics, permissions
from .models import SharedFile
from .serializers import SharedFileSerializer
from .serializers import UserRegisterSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

class SharedFileUploadView(generics.CreateAPIView):
    queryset = SharedFile.objects.all()
    serializer_class = SharedFileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(uploader=self.request.user)

class SharedFileListView(generics.ListAPIView):
    serializer_class = SharedFileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return SharedFile.objects.filter(recipient=self.request.user)

class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer    

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})   

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
      
