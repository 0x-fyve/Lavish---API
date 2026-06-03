from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()



class Transaction(models.Model):

    INCOME = "income"
    EXPENSE = "expense"

    TYPE_CHOICES = [
        (INCOME, "Income"),
        (EXPENSE, "Expense"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    #category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    date = models.DateField()

class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=50)
    limit = models.DecimalField(max_digits=10, decimal_places=2)    
