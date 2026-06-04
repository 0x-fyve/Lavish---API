from rest_framework import serializers
from .models import Transaction, Category, Budget
from django.contrib.auth import get_user_model

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            "id",
            "name",
            "category_type",
            "created_at" 
        ]



class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            
            "transaction_type"
            "amount",
            "category",
            "description",
            "date",
        ]


    def validate_amount(self, value):

            if value <= 0:
                raise serializers.ValidationError(
                    "Amount must be greater than zero."
                )

            return value
    def validate_amount(self, value):

        if value <= 0:
            raise serializers.ValidationError(
                "Amount must be greater than zero."
            )

        return value
  

