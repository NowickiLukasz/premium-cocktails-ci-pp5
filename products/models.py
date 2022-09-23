from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """Category Model"""
    title = models.CharField(max_length=254)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "categories"


class Product(models.Model):
    """Product MOdel"""
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField()
    abv = models.DecimalField(max_digits=3, decimal_places=1)
    has_abv = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name


class ProductReview(models.Model):
    """ Model for product review"""

    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=25, null=False, blank=False)
    user_review = models.TextField(max_length=250, null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title