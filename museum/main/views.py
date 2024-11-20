from django.shortcuts import render
from .models import Exhibition


def index(request):
    return render(request, 'main/index.html')


def rooms_list(request):
    return render(request, 'main/rooms-list.html')


def exhibitons_list(request):
    exhibitions = Exhibition.objects.all()
    return render(request, 'main/exhibitions-list.html', {'exhibitions': exhibitions})

def exhibits_list(request):
    return render(request,'main/exhibits-list.html')
