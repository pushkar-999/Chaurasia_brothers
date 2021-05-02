from django.db import models
from display_app.models import Products
from CRM.models import Sales_Orders

# Create your models here.

Availablity_CHOICES = (
    ('Available', 'Available'),
    ('Below Reorder level', 'Below_Reorder_level'),
    ('Out of Stock', 'Out_of_Stock')
)




class Inventory(models.Model):
    Product = models.ForeignKey(Products, on_delete=models.PROTECT)
    available_qty = models.IntegerField(default='0')
    Availablity_status = models.CharField(choices=Availablity_CHOICES, max_length=19, default='Out of Stock')
    reorder_level = models.PositiveSmallIntegerField(default='2')
    target_level = models.PositiveIntegerField(default='10')

    def __str__(self):
        return self.Product
    
    def shelve_status(self):
        if self.available_qty == 0:
            if 0 < self.available_qty > self.reorder_level:
                return "Item to be Ordred."
            return "Item is out of stock."
        else:
            return "Item is available on the shelves."



class Sales_Orders_Details(models.Model):
    Sales_Order = models.ForeignKey(Sales_Orders, on_delete=models.PROTECT)
    Product = models.ForeignKey(Products, on_delete=models.PROTECT)
    qty = models.PositiveIntegerField(default='0')
    total_value = models.PositiveIntegerField()
    tax = models.PositiveSmallIntegerField()
    amount = models.PositiveIntegerField()

