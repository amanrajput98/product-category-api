from django.db import models

# Create your models here.


class Categories(models.Model):
    """Model for Categories in Application"""
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class Products(models.Model):
    """Model for Products in Application"""
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    product_price = models.FloatField()
    product_desc = models.TextField()
    product_image = models.ImageField(upload_to=r"ProductCatApp/products_images")

    def __str__(self):
        return self.product_name
