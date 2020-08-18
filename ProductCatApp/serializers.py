from rest_framework import serializers

from ProductCatApp import models


class CategorySerializer(serializers.ModelSerializer):
    """Serialixes a Category object"""

    class Meta:
        model = models.Categories
        fields = ('category_name',)


class ProductSerializer(serializers.ModelSerializer):
    """Serialixes a Product object"""

    class Meta:
        model = models.Products
        fields = (
            'category',
            'product_name',
            'product_price',
            'product_desc',
            'product_image'
        )
