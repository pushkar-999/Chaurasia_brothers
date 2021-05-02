from django.contrib import admin
from django.urls import path
from Inventory_managment import views



urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("partners", views.partners, name='partners'),
    path("contacts", views.contacts, name='contacts'),
    path("products", views.products, name='products'),
    path("productdetails", views.productdetails, name='productdetails'),
]
