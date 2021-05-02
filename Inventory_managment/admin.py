from django.contrib import admin

# Register your models here.


from .models import Inventory, Sales_Orders_Details

admin.site.register(Inventory)
admin.site.register(Sales_Orders_Details)