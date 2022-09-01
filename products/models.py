from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=254)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "categories"


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    description = models.TextField()
    abv = models.DecimalField(max_digits=3, decimal_places=1)
    has_abv = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.name
