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
    
    def validate_category(self, category):

        user = self.context["request"].user

        if category.user != user:
            raise serializers.ValidationError(
                "Invalid category."
            )

        return category

    def validate(self, attrs):

        category = attrs["category"]
        transaction_type = attrs["transaction_type"]

        if category.category_type != transaction_type:
            raise serializers.ValidationError(
                {
                    "transaction_type":
                    "Must match category type."
                }
            )

        return attrs
    
class BudgetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Budget
        fields = [
            "id",
            "category",
            "limit"
        ]


