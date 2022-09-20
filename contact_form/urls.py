from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_us, name='contact_us'),
    path('contact_list', views.contact_us_list, name='contact_us_list'),
]
