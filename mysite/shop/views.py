from django.shortcuts import get_object_or_404,render
from django.template import loader
from django.http import HttpResponse
from .models import Product
# Create your views here.

def index(request):
    view_title = "Home"
    product_list = Product.objects.all()
    template = loader.get_template('shop/index.html')
    context = {
        'product_list': product_list,
        'view_title':view_title,
    }
    return HttpResponse(template.render(context, request))
    #return render(request, 'shop/index.html')

def detail(request, product_id):
    view_title = "Product Details"
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'shop/product-details.html', {'product': product,'view_title':view_title})

def cart(request):
    view_title = "Cart"
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
        'view_title':view_title,
    }
    return HttpResponse(template.render(context, request))


def checkout(request):
    view_title = "Checkout"
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
        'view_title':view_title,
    }
    return HttpResponse(template.render(context, request))

def simpleChart(request):
    view_title = "Simple Chart"
    #template = loader.get_template('analytics/simpleChart.html')
    #return HttpResponse(template.render(context, request))
    context = {
        'view_title':view_title,
    }
    return render(request, 'analytics/simpleChart.html',context)

def multiChart(request):
    view_title = "Real Time - Multichart"
    #template = loader.get_template('analytics/multiChart.html')
    #return HttpResponse(template.render(context, request))
    context = {
        'view_title':view_title,
    }
    return render(request, 'analytics/multichart.html',context)

def thanks(request):
    view_title = "Thanks"
    context = {
        'view_title':view_title,
    }
    return render(request, 'shop/thanks.html',context)
