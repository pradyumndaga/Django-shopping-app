import json
from pydoc import describe
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.core import serializers

from products.forms import ProductForm
from products.models import Products

# Create your views here.
def registerProduct(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product_data = ProductForm(data=data)
        print(data)
        if product_data.is_valid():
            product = product_data.save()
            product.save()
            return HttpResponse('Product Added Successfully')
        else:
            print(ProductForm.errors)

def getProducts(request):
    data = serializers.serialize("json", Products.objects.all());
    json_data = {"SomeModel_json": data}
    return JsonResponse(data, safe=False)