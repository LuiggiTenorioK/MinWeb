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
    subtotal = 0.0
    total = 0.0
    for product in product_list:
        subtotal += product.price*product.state
    total = subtotal + 3.0
    context = {
        'product_list': product_list,
        'subtotal':subtotal,
        'total':total,
    }
    return HttpResponse(template.render(context, request))


def checkout(request):
    product_list = Product.objects.filter(state__gt=0)
    template = loader.get_template('shop/checkout.html')
    subtotal = 0.0
    total = 0.0
    for product in product_list:
        subtotal += product.price*product.state
    total = subtotal + 3.0
    context = {
        'product_list': product_list,
        'subtotal':subtotal,
        'total':total,
    }
    return HttpResponse(template.render(context, request))

def simpleChart(request):
    #template = loader.get_template('analytics/simpleChart.html')
    #return HttpResponse(template.render(context, request))
    return render(request, 'analytics/simpleChart.html')

def multiChart(request):
    #template = loader.get_template('analytics/multiChart.html')
    #return HttpResponse(template.render(context, request))
    return render(request, 'analytics/multiChart.html')

def thanks(request):
    return render(request, 'shop/thanks.html')
