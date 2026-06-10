from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ViewSet
from .serializer import MembershipSerializer, PaymentSerializer
from .models import Membership, Payment
from account.permissions import IsOwner
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status



class MembershipView(ModelViewSet):
    serializer_class = MembershipSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        print("current_userr:", user.username, user.is_owner)

        if user.is_owner or user.is_superuser:
            return Membership.objects.all()
        
        return Membership.objects.filter(user=user)
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if not queryset.exists():
            return Response({"message": "No memberships", "data": []}, status=status.HTTP_200_OK)
        serializer = self.get_serializer(queryset, many=True)
        return Response({"message": "membership fetched successfully", "data": serializer.data})

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PaymentView(ModelViewSet):
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        if user.is_owner or user.is_superuser:
            return Payment.objects.all()
        
        return Payment.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, status="SUCCESS")



    


