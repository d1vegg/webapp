from django.shortcuts import render

# Create your views here.

def orders_home(request):
    return render(request,'orders/orders_home.html')