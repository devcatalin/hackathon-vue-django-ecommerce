from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError

from .models import Category, Subcategory, Product

from .services import create_product

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


class SellerProductListView(APIView):
    def get(self, request, *args, **kwargs):
        products = Product.objects.filter(owner=request.user)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductCreateView(APIView):
    class InputSerializer(serializers.Serializer):
        title = serializers.CharField()
        price = serializers.DecimalField(max_digits=6, decimal_places=2)
        description = serializers.CharField()
        thumbnail = serializers.ImageField()
        subcategory = serializers.SlugField()

    def post(self, request, *args, **kwargs):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        create_product(owner=request.user, **serializer.validated_data)

        return Response("Created successfully")


class ProductDetailView(APIView):
    authentication_classes = []
    permission_classes = []

    class InputSerializer(serializers.Serializer):
        product_slug = serializers.IntegerField()

    def post(self, request, *args, **kwargs):
        input_serializer = self.InputSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        try:
            product = Product.objects.get(
                slug=input_serializer.validated_data["product_slug"]
            )
        except Product.DoesNotExist:
            raise ValidationError("Product does not exist.")

        output_serializer = ProductSerializer(product)

        return Response(output_serializer.data)


class ProductDeleteView(APIView):
    class InputSerializer(serializers.Serializer):
        product_slug = serializers.SlugField()

    def post(self, request, *args, **kwargs):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        product_slug = serializer.validated_data["product_slug"]

        if not Product.objects.filter(slug=product_slug).exists():
            raise ValidationError("Product does not exist.")

        Product.objects.filter(slug=product_slug).delete()

        return Response("Deleted successfully")
