from django.shortcuts import render
from .models import Products
from django.views.generic import ListView, DetailView, View

# Create your views here.
def index(request):
    return render(request,'index.html',)

def about(request):
    return render(request,'about.html')

def partners(request):
    return render(request,'partners.html')

def contacts(request):
    return render(request,'contacts.html')

def productdetails(request):
    context = {
        'product' : Products.objects.all()
    }
    return render(request,'productdetails.html', context)

class ProductList(ListView):
    model = Products
    paginate_by = 4
    template_name = "Products.html"
   
def products(request):
    context = {
            'product' : Products.objects.all()
         }
    return render(request,'productdetails.html', context)

class ProductDetailView(DetailView):
    model = Products
    template_name = "product.html"
