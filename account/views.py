from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import SignupSerializer, UserSerializer, SumSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import User
from rest_framework.permissions import IsAuthenticated
from account.permissions import IsOwner
from rest_framework.viewsets import ModelViewSet

class SignUp(APIView):
    def post(self, request):
        data = request.data
        serializer = SignupSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User created successfully"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsOwner]


    



