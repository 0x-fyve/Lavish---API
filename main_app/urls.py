from django.urls import path
from .views import (
    CategoryListCreateView,
    CategoryDetailView, TransactionListCreateView, TransactionDetialView,
    AnalyticsSummaryView
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
        "transactions/<int:pk>",
        TransactionDetialView.as_view()
    ),
    path(
        "analytics/summary",
        AnalyticsSummaryView.as_view()
    )
]