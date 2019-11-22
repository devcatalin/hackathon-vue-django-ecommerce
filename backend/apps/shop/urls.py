from django.urls import path

from .views import (
    CategoryListView,
    ProductListView,
    ProductCreateView,
    ProductDeleteView
)

urlpatterns = [
    path('categories/', CategoryListView.as_view()),
    path('products/', ProductListView.as_view()),
    path('products/create/', ProductCreateView.as_view()),
    path('products/delete/', ProductDeleteView.as_view())
]
