from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import UpdateView, DeleteView
from django.db.models.functions import Substr

from .forms import ExhibitionForm, MuseumRoomForm, ExhibitForm, ExhibitMuseumForm
from .models import Exhibition, MuseumRoom, Exhibit, Museum


def index(request):
    return render(request, 'main/index.html')


def rooms_list(request):
    rooms = MuseumRoom.objects.all().order_by('room_number')
    return render(request, 'main/rooms-list.html', {'rooms': rooms})


def exhibitions_list(request):
    exhibitions = Exhibition.objects.all()
    return render(request, 'main/exhibitions-list.html', {'exhibitions': exhibitions})


def all_exhibits_list(request):
    sort = request.GET.get('sort', '')

    # Сортировка по выбранному параметру
    if sort == 'date':
        exhibits = Exhibit.objects.order_by('creation_year')
    elif sort == 'name':
        exhibits = Exhibit.objects.order_by(Substr('name', 1, 1))
    elif sort == 'room':
        exhibits = Exhibit.objects.order_by('room__room_number')
    else:
        exhibits = Exhibit.objects.all()
    return render(request, 'main/all-exhibits-list.html', {'exhibits': exhibits})


def exhibits_list(request, room_id):
    room = MuseumRoom.objects.get(room_id=room_id)
    exhibits = Exhibit.objects.filter(room=room)
    return render(request, 'main/exhibits-list.html', {'exhibits': exhibits, 'room': room})


class ExhibitionUpdateView(UpdateView):
    model = Exhibition
    template_name = 'main/edits/update-exhibition.html'
    form_class = ExhibitionForm


class ExhibitionDeleteView(DeleteView):
    model = Exhibition
    template_name = 'main/edits/confirm-delete-exhibition.html'
    success_url = '/exhibitions/'


class MuseumRoomDeleteView(DeleteView):
    model = MuseumRoom
    template_name = 'main/edits/confirm-delete-museum-room.html'
    success_url = '/rooms/'


class ExhibitDeleteView(DeleteView):
    model = Exhibit
    template_name = "main/edits/confirm-delete-exhibit.html"
    success_url = '/exhibits/'


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


class ExhibitUpdateView(UpdateView):
    model = Exhibit
    template_name = 'main/edits/update-exhibit.html'
    form_class = ExhibitForm


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


def add_exhibit(request):
    error = ''
    exhibits = Exhibit.objects.all()
    if request.method == 'POST':
        form = ExhibitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_exhibits_list')
        else:
            error = 'Форма была неверной'

    form = ExhibitForm()
    data = {
        'exhibits': exhibits,
        'form': form,
        'error': error

    }
    return render(request, 'main/edits/add-exhibit.html', data)


def add_exhibit_to_room(request, room_id):
    error = ''
    room = get_object_or_404(MuseumRoom, pk=room_id)

    if request.method == "POST":
        form = ExhibitMuseumForm(request.POST)
        if form.is_valid():
            exhibit = form.save(commit=False)
            exhibit.room = room
            exhibit.save()
            return redirect('exhibits_list', room_id=room_id)
    else:
        form = ExhibitMuseumForm()
        data = {
            'room': room,
            'form': form,
            'error': error
        }

    return render(request, 'main/edits/add-exhibit-to-room.html', data)
