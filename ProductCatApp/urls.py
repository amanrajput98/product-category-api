from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ProductCatApp import views

router = DefaultRouter()
router.register('category', views.CategoryViewSet)
router.register('product', views.ProductViewSet)


urlpatterns = [
    path('', include(router.urls))
]