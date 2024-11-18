from django.shortcuts import render


def index(request):
    return render(request,'main/index.html')

def rooms_list(request):
    return render(request,'main/rooms-list.html')
