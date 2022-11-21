from dataclasses import fields
from decimal import Decimal
from rest_framework import serializers
from store.models import Product, Collection, Review


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count']

    products_count = serializers.IntegerField(read_only=True)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'inventory', 'tax', 'total_price', 'collection']
    
    tax = serializers.SerializerMethodField(method_name='calculate_tax')
    total_price = serializers.SerializerMethodField(method_name='calculate_total_price')
    collection = serializers.HyperlinkedRelatedField(
        queryset = Collection.objects.all(),
        view_name='collection-detail'
    )

    def calculate_tax(self, product: Product):
        return product.price * Decimal(0.01)

    def calculate_total_price(self, product: Product):
        return product.price + (product.price * Decimal(0.01))

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'name', 'date', 'description', 'product']
