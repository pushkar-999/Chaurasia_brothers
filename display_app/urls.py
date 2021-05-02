from django.contrib import admin
from django.urls import path
from display_app import views


urlpatterns = [
    path("", views.products, name='home'),
]
