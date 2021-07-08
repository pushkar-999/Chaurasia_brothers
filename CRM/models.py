from django.db import models
from django.db.models.enums import Choices

# Create your models here.

class customers(models.Model):
    firstName= models.CharField(max_length=25, null=True, blank=True)
    lastName= models.CharField(max_length=25, null=True, blank=True)
    Company = models.CharField(max_length=50, default='General')
    contact_no= models.CharField(max_length=10)
    email= models.EmailField()

    def __str__(self):
        return self.firstName+' '+ self.lastName
    

ADDRESS_TYPE =(
    ('home', 'home'),
    ('office', 'office'),
    ('billing', 'billing'),
    ('shipping', 'shipping')
)

class addresses(models.Model):
    customer = models.ForeignKey(customers, on_delete= models.CASCADE)
    address_type = models.CharField(choices= ADDRESS_TYPE, max_length=10, default= 'home')
    firstLine= models.CharField(max_length=50)
    secondline = models.CharField(max_length=50, null= True, blank=True)
    Block = models.CharField(max_length=25)
    District = models.CharField(max_length=25)
    State = models.CharField(max_length=25)
    pin = models.IntegerField()

TRANSACTION_TYPE =(
   ('SALES','SALES'),
   ('PURCHASE','PURCHASE'),
   ('PAYMENT IN', 'PAYMENT IN'),
   ('PAYMENT OUT', 'PAYMENT OUT'),
   ('SALE RETURN', 'SALE RETURN'),
   ('PURCHASE RETURN', 'PURCHASE RETURN')
)
class transactions(models.Model):
    transactionType= models.CharField(choices= TRANSACTION_TYPE, max_length= 19, default= 'Sales')

