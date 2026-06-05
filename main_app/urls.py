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
        "transaction/",
        CategoryListCreateView.as_view(
        )
    ),
    path(
        "transaction/",
        TransactionListCreateView.as_view()
    ),
    path(
        "transaction/",
        TransactionDetialView.as_view()
    ),
]