from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('cocktails/', views.all_cocktails, name='all_cocktails'),
    path('books/', views.all_books, name='all_books'),
    path('products/<product_id>', views.product_details_page, name='product_details_page'),
    path('add/', views.add_product, name='add_product'),
]
