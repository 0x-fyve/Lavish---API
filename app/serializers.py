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


class TransactionSerializer(serializers.ModelSerializer):

    category_name = serializers.CharField(
        source="category.name",
        read_only=True
    )

    class Meta:
        model = Transaction
        fields = [
            "id",
            "category",
            "category_name",
            "amount",
            "transaction_type",
            "description",
            "date",
        ]


    def validate_amount(self, value):

        if value <= 0:
            raise serializers.ValidationError(
                "Amount must be greater than zero."
            )

        return value
    
    def validate(self, attrs):

        if (
            attrs["transaction_type"] == "expense"
            and attrs["amount"] > 1000000
        ):
            raise serializers.ValidationError(
                "Expense too large."
            )
        return attrs
  

