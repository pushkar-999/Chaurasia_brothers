from django.db import models
from django.db.models.deletion import PROTECT
from django.db.models.fields import CharField

# Create your models here.
class suppliers(models.Model):
    company=models.CharField(max_length=50)
    contactPerson=models.CharField(max_length=50)
    contact_no1= models.CharField(max_length=10)
    email= models.EmailField()

ADDRESS_TYPE =(
    ('home', 'home'),
    ('office', 'office'),
    ('billing', 'billing'),
    ('shipping', 'shipping')
)

class addresses(models.Model):
    customer = models.ForeignKey(suppliers, on_delete= models.CASCADE)
    address_type = models.CharField(choices= ADDRESS_TYPE, max_length=10, default= 'home')
    firstLine= models.CharField(max_length=50)
    secondline = models.CharField(max_length=50, null= True, blank=True)
    Block = models.CharField(max_length=25)
    District = models.CharField(max_length=25)
    State = models.CharField(max_length=25)
    pin = models.IntegerField()


class purchaseOrders(models.Model):
    party = models.ForeignKey(suppliers, on_delete=PROTECT)
    