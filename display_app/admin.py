from django.contrib import admin

# Register your models here.
from .models import brand, section, Products


admin.site.register(brand)
admin.site.register(section)
admin.site.register(Products)