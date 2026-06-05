from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from .models import Category

User = get_user_model()


@receiver(post_save, sender=User)
def create_default_categories(sender, instance, created, **kwargs):

    if created:

        expense_categories = [
            "Food",
            "Transport",
            "Rent",
            "Utilities",
            "Entertainment",
            "Healthcare",
        ]

        income_categories = [
            "Salary",
            "Freelance",
            "Business",
            "Investment",
            "Gift",
        ]

        categories = []

        for name in expense_categories:
            categories.append(
                Category(
                    user=instance,
                    name=name,
                    category_type="expense"
                )
            )

        for name in income_categories:
            categories.append(
                Category(
                    user=instance,
                    name=name,
                    category_type="income"
                )
            )

        Category.objects.bulk_create(categories)