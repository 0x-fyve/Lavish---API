from rest_framework import serializers
from .models import Expense, Income, Budget


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = [
            "title",
            "amount",
            "category",
            "date",
        ]

        def create(self, request, validated_data):
            Expense.objects.create(
                user = request.user,
                title = validated_data["title"],
                amount = validated_data["amount"],
                category = validated_data["category"],
                date = validated_data["date"]
            )