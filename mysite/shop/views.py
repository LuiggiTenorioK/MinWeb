from django.shortcuts import get_object_or_404,render
from django.template import loader
from django.http import HttpResponse
from .models import Product
# Create your views here.

def index(request):
    product_list = Product.objects.all()
    template = loader.get_template('shop/index.html')
    context = {
        'product_list': product_list,
    }
    return HttpResponse(template.render(context, request))
    #return render(request, 'shop/index.html')

def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'shop/product-details.html', {'product': product})

def cart(request):
    product_list = Product.objects.filter(state__gt=0)
    template = loader.get_template('shop/cart.html')
    context = {
        'product_list': product_list,
    }
    
    return HttpResponse(template.render(context, request))
