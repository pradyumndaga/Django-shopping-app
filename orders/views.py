from datetime import datetime
import json
from django.http import HttpResponse, JsonResponse
from django.core import serializers
import datetime
from orders.forms import OrderForm
from orders.models import Orders
from django.db.models import Q

# Create your views here.
def createOrder(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        date = datetime.datetime.now().time()
        order_data = OrderForm(data=data)
        print(order_data)
        if order_data.is_valid():
            order = order_data.save()
            order.save()
            return HttpResponse('Order created Successfully')
        else:
            print(order_data.errors)

def getOrders(request):
    data = serializers.serialize("json", Orders.objects.all())
    return JsonResponse(data, safe=False)

def getOrdersInInterval(request):
    data = json.loads(request.body)
    # datetime.timedelta(days= data.date)
    
    print('date', data['date'])
    print('orders',Orders.objects, 'class', type(Orders.objects))
    orders = Orders.objects.filter(purchase_date__gte =  data['date'])
    data = serializers.serialize("json", orders)
    return JsonResponse(data, safe=False)