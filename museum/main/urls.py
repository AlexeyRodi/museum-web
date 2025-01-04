from django.urls import path
from . import views
from . import views_api

urlpatterns = [
    path('', views.index, name='index'),
    path('rooms/', views.rooms_list, name='rooms_list'),
    path('exhibitions/', views.exhibitions_list, name='exhibitions_list'),
    path('exhibits/', views.all_exhibits_list, name='all_exhibits_list'),
    path('rooms/<int:room_id>/exhibits/', views.exhibits_list, name='exhibits_list'),
    path('exhibitions/add/', views.add_exhibition, name='add_exhibition'),
    path('rooms/add/', views.add_museum_room, name='add_museum_room'),
    path('exhibits/add/', views.add_exhibit, name='add_exhibit'),
    path('add_exhibit_to_room/<int:room_id>/', views.add_exhibit_to_room, name='add_exhibit_to_room'),
    path('exhibitions/edit/<int:pk>/', views.ExhibitionUpdateView.as_view(), name='update_exhibition'),
    path('rooms/edit/<int:pk>', views.MuseumRoomUpdateView.as_view(), name='update_museum_room'),
    path('exhibits/edit/<int:pk>', views.ExhibitUpdateView.as_view(), name='update_exhibit'),
    path('exhibitions/delete/<int:pk>', views.ExhibitionDeleteView.as_view(), name='delete_exhibition'),
    path('rooms/delete/<int:pk>', views.MuseumRoomDeleteView.as_view(), name='delete_museum_room'),
    path('exhibits/delete/<int:pk>', views.ExhibitDeleteView.as_view(), name='delete_exhibit'),
    path('exhibitions/<int:exhibition_id>/', views.exhibition_detail, name='exhibition_detail'),
    path('exhibits/<int:exhibit_id>/',views.exhibit_detail,name='exhibit_detail'),
    path('rooms/<int:room_id>/exhibits/<int:exhibit_id>/',views.exhibit_room_detail,name='exhibit_room_detail'),


    path('api/exhibitions/', views_api.ExhibitionsAPI.as_view(), name='exhibitions-list-api'),
    path('api/rooms/', views_api.MuseumRoomAPI.as_view(), name='museum-rooms-list-api'),

]
