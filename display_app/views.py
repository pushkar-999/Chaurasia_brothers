from django.shortcuts import render
from .models import Products

# Create your views here.
def products(request):
    context = {
        'Products': Products.objects.all()
    }
    return render(request,'disProducts.html',context)
