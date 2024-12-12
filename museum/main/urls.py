from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rooms/', views.rooms_list, name='rooms_list'),
    path('exhibitions/', views.exhibitons_list, name='exhibitions_list'),
    path('exhibits/', views.exhibits_list, name='exhibits_list'),
    path('exhibits/<int:room_id>/', views.exhibits_list, name='exhibits_list'),
    path('exhibitions/add/', views.add_exhibition, name='add_exhibition'),
    path('rooms/add/', views.add_museum_room, name='add_museum_room'),
    path('<int:pk>/exhibitions/edit/',views.ExhibitionUpdateView.as_view(), name='update_exhibition'),
    path('<int:pk>/rooms/edit/',views.MuseumRoomUpdateView.as_view(), name='update_museum_room'),
    path('<int:pk>/exhibitions/delete/',views.ExhibitionDeleteView.as_view(), name='delete_exhibition'),
    path('<int:pk>/rooms/delete/',views.MuseumRoomDeleteView.as_view(), name='delete_museum_room')
]
