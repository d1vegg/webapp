from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html', {'title':'Главная страница'})


def buying(request):
    return render(request, 'main/buying.html')


def selling(request):
    return render(request, "main/selling.html")