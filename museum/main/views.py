from django.shortcuts import render, redirect

from .forms import ExhibitionForm
from .models import Exhibition, Museum_Room, Exhibit, Museum


def index(request):
    return render(request, 'main/index.html')


def rooms_list(request):
    rooms = Museum_Room.objects.all()
    return render(request, 'main/rooms-list.html', {'rooms': rooms})


def exhibitons_list(request):
    exhibitions = Exhibition.objects.all()
    return render(request, 'main/exhibitions-list.html', {'exhibitions': exhibitions})


def exhibits_list(request, room_id):
    room = Museum_Room.objects.get(room_id=room_id)
    exhibits = Exhibit.objects.filter(room=room)
    return render(request, 'main/exhibits-list.html', {'exhibits': exhibits, 'room': room})


def add_exhibition(request):
    error = ''
    museums = Museum.objects.all()
    if request.method == 'POST':
        form = ExhibitionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exhibitions_list')
        else: error = 'Форма была неверной'

    form = ExhibitionForm()
    data = {
        'museums' : museums,
        'form': form,
        'error' : error
    }
    return render(request, 'main/edits/add-exhibition.html', data)
