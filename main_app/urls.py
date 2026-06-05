from django.urls import path
from .views import (
    CategoryListCreateView,
    CategoryDetailView, TransactionListCreateView, TransactionDetialView
)

urlpatterns = [
    path(
        "categories/",
        CategoryListCreateView.as_view()
    ),
    path(
        "categories/<int:pk>/",
        CategoryDetailView.as_view()
    ),
    path(
        "transactions/",
        TransactionListCreateView.as_view()
    ),
    path(
        "transaction/<int:>",
        TransactionDetialView.as_view()
    ),
]