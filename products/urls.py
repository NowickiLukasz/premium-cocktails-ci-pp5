from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('cocktails/', views.all_cocktails, name='all_cocktails'),
    path('books/', views.all_books, name='all_books'),
]
