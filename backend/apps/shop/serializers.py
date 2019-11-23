from rest_framework import serializers

from .models import Category, Subcategory, Product


class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ['title', 'slug']


class CategorySimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'slug']


class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubcategorySerializer(many=True)
    class Meta:
        model = Category
        fields = ['title', 'slug', 'subcategories']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySimpleSerializer(source="subcategory.category")
    subcategory = SubcategorySerializer()
    seller = serializers.CharField(source="owner.username")
    class Meta:
        model = Product
        fields = [
            'seller',
            'slug',
            'title',
            'price',
            'description',
            'quantity_type',
            'quantity',
            'thumbnail',
            'category',
            'subcategory'
        ]
