from django.db import models

# Create your models here.
class cashIn(models.Model): 
    cash = models.CharField(max_length=10)