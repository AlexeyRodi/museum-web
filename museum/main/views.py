from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import UpdateView, DeleteView
from django.db.models.functions import Substr
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .forms import ExhibitionForm, MuseumRoomForm, ExhibitForm, ExhibitMuseumForm
from .models import Exhibition, MuseumRoom, Exhibit, Museum


def index(request):
    return render(request, 'main/index.html')


from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def rooms_list(request):
    search_query = request.GET.get('q', '')
    sort = request.GET.get('sort', '')

    rooms = MuseumRoom.objects.all()

    if search_query:
        rooms = rooms.filter(room_number__icontains=search_query)

    if sort == 'number':
        rooms = rooms.order_by('room_number')
    elif sort == 'description':
        rooms = rooms.order_by('description')

    paginator = Paginator(rooms, 10)
    page = request.GET.get('page')

    try:
        rooms_page = paginator.page(page)
    except PageNotAnInteger:
        rooms_page = paginator.page(1)
    except EmptyPage:
        rooms_page = paginator.page(paginator.num_pages)

    return render(request, 'main/rooms-list.html', {
        'rooms': rooms_page,
        'search_query': search_query,
    })


def exhibitions_list(request):
    search_query = request.GET.get('q', '')
    sort = request.GET.get('sort', '')
    exhibitions = Exhibition.objects.all()

    if search_query:
        exhibitions = exhibitions.filter(name__icontains=search_query)

    if sort == 'name':
        exhibitions = exhibitions.order_by(Substr('name', 1, 1))

    paginator = Paginator(exhibitions, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'main/exhibitions-list.html', {
        'exhibitions': page_obj,
        'search_query': search_query
    })


def all_exhibits_list(request):
    sort = request.GET.get('sort', '')
    search_query = request.GET.get('q', '')

    exhibits = Exhibit.objects.all()

    if search_query:
        exhibits = exhibits.filter(name__icontains=search_query)

    if sort == 'date':
        exhibits = exhibits.order_by('creation_year')
    elif sort == 'name':
        exhibits = exhibits.order_by(Substr('name', 1, 1))
    elif sort == 'room':
        exhibits = exhibits.order_by('room__room_number')

    paginator = Paginator(exhibits, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'main/all-exhibits-list.html', {
        'exhibits': page_obj,
        'search_query': search_query
    })


def exhibits_list(request, room_id):
    room = MuseumRoom.objects.get(room_id=room_id)
    sort = request.GET.get('sort', '')
    search_query = request.GET.get('q', '')

    exhibits = Exhibit.objects.filter(room=room)

    if search_query:
        exhibits = exhibits.filter(name__icontains=search_query)

    if sort == 'date':
        exhibits = exhibits.order_by('creation_year')
    elif sort == 'name':
        exhibits = exhibits.order_by(Substr('name', 1, 1))
    elif sort == 'room':
        exhibits = exhibits.order_by('room__room_number')

    paginator = Paginator(exhibits, 10)
    page = request.GET.get('page')

    try:
        exhibits_page = paginator.page(page)
    except PageNotAnInteger:
        exhibits_page = paginator.page(paginator.num_pages)

    return render(request, 'main/exhibits-list.html', {
        'exhibits': exhibits_page,
        'room': room,
        'search_query': search_query
    })


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
        form = ExhibitionForm(request.POST, request.FILES)
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
        form = ExhibitForm(request.POST, request.FILES)
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
        form = ExhibitMuseumForm(request.POST, request.FILES)
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


def exhibition_detail(request, exhibition_id):
    exhibition = get_object_or_404(Exhibition, exhibition_id=exhibition_id)
    return render(request, 'main/exhibition-detail.html', {'exhibition': exhibition})


def exhibit_detail(request, exhibit_id):
    exhibit = get_object_or_404(Exhibit, exhibit_id=exhibit_id)
    return render(request, 'main/exhibit-detail.html', {'exhibit': exhibit})


def exhibit_room_detail(request, exhibit_id, room_id):
    exhibit = get_object_or_404(Exhibit, exhibit_id=exhibit_id)
    room = get_object_or_404(MuseumRoom, room_id=room_id)
    return render(request, 'main/exhibit-room-detail.html', {'exhibit': exhibit, 'room': room})
