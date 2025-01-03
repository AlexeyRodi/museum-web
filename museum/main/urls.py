from django.urls import path
from . import views
from . import views_api

urlpatterns = [
    path('', views.index, name='index'),
    path('rooms/', views.rooms_list, name='rooms_list'),
    path('exhibitions/', views.exhibitions_list, name='exhibitions_list'),
    path('exhibits/', views.all_exhibits_list, name='all_exhibits_list'),
    path('exhibits/<int:room_id>/', views.exhibits_list, name='exhibits_list'),
    path('exhibitions/add/', views.add_exhibition, name='add_exhibition'),
    path('rooms/add/', views.add_museum_room, name='add_museum_room'),
    path('exhibits/add/', views.add_exhibit, name='add_exhibit'),
    path('add_exhibit_to_room/<int:room_id>/', views.add_exhibit_to_room, name='add_exhibit_to_room'),
    path('<int:pk>/exhibitions/edit/', views.ExhibitionUpdateView.as_view(), name='update_exhibition'),
    path('<int:pk>/rooms/edit/', views.MuseumRoomUpdateView.as_view(), name='update_museum_room'),
    path('<int:pk>/exhibits/edit/', views.ExhibitUpdateView.as_view(), name='update_exhibit'),
    path('<int:pk>/exhibitions/delete/', views.ExhibitionDeleteView.as_view(), name='delete_exhibition'),
    path('<int:pk>/rooms/delete/', views.MuseumRoomDeleteView.as_view(), name='delete_museum_room'),
    path('<int:pk>/exhibits/delete/', views.ExhibitDeleteView.as_view(), name='delete_exhibit'),
    path('exhibition/<int:exhibition_id>/', views.exhibition_detail, name='exhibition_detail'),


    path('api/exhibitions/', views_api.ExhibitionsAPI.as_view(), name='exhibitions-list-api'),
    path('api/rooms/', views_api.MuseumRoomAPI.as_view(), name='museum-rooms-list-api'),

]
