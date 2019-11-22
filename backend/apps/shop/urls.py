from django.urls import path

from .views import CategoryListView, ProductListView

urlpatterns = [
    path('categories/', CategoryListView.as_view()),
    path('products/', ProductListView.as_view())
]
