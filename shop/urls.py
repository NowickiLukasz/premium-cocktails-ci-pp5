from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop_page, name='shop'),
    path('newsletter/', views.newsletter_application, name='newsletter'),
]
