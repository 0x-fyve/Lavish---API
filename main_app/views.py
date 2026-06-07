from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import TransactionSerializer, CategorySerializer
from .models import Category, Transaction
from rest_framework import generics
# Create your views here.
class CategoryListCreateView(generics.ListCreateAPIView):

    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Category.objects.filter(
            user=self.request.user
        )

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user
        )    
        
class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Category.objects.filter(
            user=self.request.user
        )        
    
class TransactionListCreateView(generics.ListCreateAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(
            user = self.request.user
        ) 

    def get_queryset(self):
        query_set = []
        query_set = Transaction.objects.filter(
           user = self.request.user
        )

        transaction_type = self.request.query_params.get("type")
        category = self.request.query_params.get("category")

        start_date = self.request.query_params.get("start_date")
        end_date = self.request.query_params.get("end_date")

        if start_date:
            queryset = queryset.filter(
                date__gte=start_date
            )

        if end_date:
            queryset = queryset.filter(
                date__lte=end_date
            )

        if transaction_type:
            query_set =  Transaction.objects.filter(
                user=self.request.user,
                transaction_type=transaction_type
            )

        if category:
            query_set =  Transaction.objects.filter(
                user=self.request.user,
                category__name=category
            )        

        return query_set

class TransactionDetialView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return (
            Transaction.objects
            .filter(user=self.request.user)
            .select_related("category")
        )
    
        

            