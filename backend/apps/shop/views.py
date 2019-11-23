from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError

from apps.users.serializers import UserProfileSerializer
from apps.users.models import UserProfile

from .models import Category, Subcategory, Product

from .services import create_product

from .selectors import get_categories, get_products_from_subcategory

from .serializers import CategorySerializer, ProductSerializer

from .utils import inline_serializer


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

    class InputSerializer(serializers.Serializer):
        category = serializers.CharField(required=False, allow_blank=True)
        subcategory = serializers.CharField(required=False, allow_blank=True)
        sellers = serializers.ListField(child=serializers.CharField(), required=False)
        sort_option = serializers.CharField(required=False, allow_blank=True)

    def post(self, request, *args, **kwargs):
        input_serializer = self.InputSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        category = input_serializer.validated_data["category"] or None
        subcategory = input_serializer.validated_data["subcategory"] or None
        sellers = input_serializer.validated_data["sellers"] or None
        sort_option = input_serializer.validated_data["sort_option"] or None
        products = Product.objects.all()

        if category and category != "":
            products = products.filter(subcategory__category__slug=category)

        if subcategory and subcategory != "":
            products = products.filter(subcategory__slug=subcategory)

        print(sellers)
        if sellers and len(sellers) > 0:
            products = products.filter(owner__username__in=sellers)

        if sort_option and sort_option != "":
            products = products.order_by(sort_option)

        products_serializer = ProductSerializer(products, many=True)

        owners = set()

        for product in products:
            owners.add(product.owner.username)

        sellers = UserProfile.objects.filter(user__username__in=owners)
        sellers_serializer = UserProfileSerializer(sellers, many=True)

        return Response({
            'products': products_serializer.data,
            'sellers': sellers_serializer.data
        })


class SellerProductListView(APIView):
    def get(self, request, *args, **kwargs):
        products = Product.objects.filter(owner=request.user)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetailView(APIView):
    authentication_classes = []
    permission_classes = []

    class InputSerializer(serializers.Serializer):
        product_slug = serializers.SlugField()

    def post(self, request, *args, **kwargs):
        input_serializer = self.InputSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)

        try:
            product = Product.objects.get(
                slug=input_serializer.validated_data["product_slug"]
            )
        except Product.DoesNotExist:
            raise ValidationError("Product does not exist.")

        product_serializer = ProductSerializer(product)

        similar_products = Product.objects.filter(
            subcategory__category=product.subcategory.category
        ).exclude(slug=product.slug).order_by('?')[6:]

        similar_products_serializer = ProductSerializer(similar_products, many=True)

        return Response(
            {
                "product": product_serializer.data,
                "similar_products": similar_products_serializer.data
            }
        )


class ProductCreateView(APIView):
    class InputSerializer(serializers.Serializer):
        title = serializers.CharField()
        price = serializers.DecimalField(max_digits=6, decimal_places=2)
        description = serializers.CharField()
        thumbnail = serializers.ImageField()
        quantity_type = serializers.CharField()
        subcategory = serializers.SlugField()

    def post(self, request, *args, **kwargs):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        create_product(owner=request.user, **serializer.validated_data)

        return Response("Created Product successfully!")


class ProductUpdateView(APIView):
    class InputSerializer(serializers.Serializer):
        product_slug = serializers.SlugField()
        title = serializers.CharField(required=False)
        price = serializers.DecimalField(max_digits=6, decimal_places=2, required=False)
        description = serializers.CharField(required=False)
        thumbnail = serializers.ImageField(required=False)
        quantity_type = serializers.CharField(required=False)
        subcategory = serializers.SlugField(required=False)

    def post(self, request, *args, **kwargs):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        update_product(owner=request.user, **serializer.validated_data)

        return Response("Updated Product successfully!")


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
