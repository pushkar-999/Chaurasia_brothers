from django.contrib import admin

# Register your models here.
from .models import customers, addresses, Sales_Orders


admin.site.register(customers)
admin.site.register(addresses)
admin.site.register(Sales_Orders)