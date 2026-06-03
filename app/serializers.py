from rest_framework import serializers
from .models import Transaction, Budget


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            "title",
            "transaction_type"
            "amount",
            "category",
            "description",
            "date",
        ]

        def create(self, request, validated_data):
            Transaction.objects.create(
                user = request.user,
                title = validated_data["title"],
                amount = validated_data["amount"],
                category = validated_data["category"],
                date = validated_data["date"]
            )