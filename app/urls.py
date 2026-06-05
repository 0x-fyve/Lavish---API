from django.urls import path
from .views import (
    CategoryListCreateView,
    CategoryDetailView,
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
]