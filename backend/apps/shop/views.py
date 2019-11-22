from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category, Subcategory, Product

from .selectors import get_categories, get_products_from_subcategory

from .serializers import CategorySerializer, ProductSerializer


class CategoryListView(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request, *args, **kwargs):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class ProductListView(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request, *args, **kwargs):
        subcategory = request.query_params.get('subcategory', None)
        if subcategory:
            products = Product.objects.filter(subcategory__slug=subcategory)
        else:
            products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
