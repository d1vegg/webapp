from django.shortcuts import render

# Create your views here.

def orders_home(request):
    return render(request,'orders/orders_home.html')


def buying(request):
    return render(request, 'orders/buying.html')


def selling(request):
    return render(request, "orders/selling.html")