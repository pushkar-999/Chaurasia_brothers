from django.contrib import admin

# Register your models here.
from .models import customers, addresses


admin.site.register(customers)
admin.site.register(addresses)