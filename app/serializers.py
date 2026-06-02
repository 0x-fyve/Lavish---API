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