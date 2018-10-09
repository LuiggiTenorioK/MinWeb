from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Product
# Create your views here.

def index(request):
    product_list = Product.objects.order_by('-name')[:5]
    template = loader.get_template('shop/index.html')
    context = {
        'product_list': product_list,
    }
    return HttpResponse(template.render(context, request))
    #return render(request, 'shop/index.html')