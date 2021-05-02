from django.db import models


# Create your models here.

TAX_CHOICES =(
    ('0%', '0%'),
    ('5%', '5%'),
    ('12%', '12%'),
    ('18%', '18%'),
    ('28%', '28%')
)


class section(models.Model):
    section = models.CharField(max_length=25, default='No section assigned')

    def __str__(self):
        return self.section

class brand(models.Model):
    brand = models.CharField(max_length=25, default= 'Not Filled')

    def __str__(self):
        return self.brand


class Products(models.Model):
    Item = models.CharField(max_length=25)
    Discription = models.CharField(max_length=225, blank=True, null=True)
    section = models.ForeignKey(section, on_delete=models.PROTECT)
    Brand = models.ForeignKey(brand, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    Tax_slab = models.CharField(choices=TAX_CHOICES, max_length=12, default='0%')

    def __str__(self):
        return self.Item


class upcoming_products(models.Model):
    Products= models.ForeignKey(Products, on_delete=models.PROTECT)
    demand= models.IntegerField()
