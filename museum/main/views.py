from django.shortcuts import render, redirect
from django.views.generic import UpdateView

from .forms import ExhibitionForm, MuseumRoomForm
from .models import Exhibition, MuseumRoom, Exhibit, Museum


def index(request):
    return render(request, 'main/index.html')


def rooms_list(request):
    rooms = MuseumRoom.objects.all().order_by('room_number')
    return render(request, 'main/rooms-list.html', {'rooms': rooms})


def exhibitons_list(request):
    exhibitions = Exhibition.objects.all()
    return render(request, 'main/exhibitions-list.html', {'exhibitions': exhibitions})


def exhibits_list(request, room_id):
    room = MuseumRoom.objects.get(room_id=room_id)
    exhibits = Exhibit.objects.filter(room=room)
    return render(request, 'main/exhibits-list.html', {'exhibits': exhibits, 'room': room})


class ExhibitionUpdateView(UpdateView):
    model = Exhibition
    template_name = 'main/edits/update-exhibition.html'
    form_class = ExhibitionForm

def add_exhibition(request):
    error = ''
    museums = Museum.objects.all()
    if request.method == 'POST':
        form = ExhibitionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exhibitions_list')
        else:
            error = 'Форма была неверной'

    form = ExhibitionForm()
    data = {
        'museums': museums,
        'form': form,
        'error': error
    }
    return render(request, 'main/edits/add-exhibition.html', data)

class MuseumRoomUpdateView(UpdateView):
    model = MuseumRoom
    template_name = 'main/edits/update-museum-room.html'
    form_class = MuseumRoomForm

def add_museum_room(request):
    error = ''
    museums = Museum.objects.all()
    if request.method == 'POST':
        form = MuseumRoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rooms_list')
        else:
            error = 'Форма была неверной'

    form = MuseumRoomForm()
    data = {
        'museums': museums,
        'form': form,
        'error': error

    }
    return render(request, 'main/edits/add-museum-room.html', data)
