from django.shortcuts import render
from . import  serializers, models
from  rest_framework import viewsets


class CategoryViewSet(viewsets.ModelViewSet):
    """Handle creating and updating categories"""
    serializer_class = serializers.CategorySerializer
    queryset = models.Categories.objects.all()


class ProductViewSet(viewsets.ModelViewSet):
    """Handle creating and updating products"""
    serializer_class = serializers.ProductSerializer
    queryset = models.Products.objects.all()