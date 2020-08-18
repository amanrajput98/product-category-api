from rest_framework import serializers

from ProductCatApp import models


class ProductSerializer(serializers.ModelSerializer):
    """Serialixes a Product object"""

    # class Meta:
    #     model = models.Products