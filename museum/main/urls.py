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
    path('exhibits/<int:exhibit_id>/', views.exhibit_detail, name='exhibit_detail'),
    path('rooms/<int:room_id>/exhibits/<int:exhibit_id>/', views.exhibit_room_detail, name='exhibit_room_detail'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),

    path('api/exhibitions/', views_api.ExhibitionsAPI.as_view(), name='exhibitions-list-api'),
    path('api/rooms/', views_api.MuseumRoomAPI.as_view(), name='museum-rooms-list-api'),
    path('api/exhibits/', views_api.ExhibitAPI.as_view(), name='exhibits-list-api'),
    path('api/exhibits/<int:pk>/', views_api.ExhibitDetailAPI.as_view(), name='exhibit-detail'),
    path('api/exhibitions/<int:pk>/', views_api.ExhibitionDetailAPI.as_view(), name='exhibition-detail'),
    path('api/exhibits/update/<int:pk>/', views_api.ExhibitUpdateView.as_view()),
    path('api/exhibitions/update/<int:pk>/', views_api.ExhibitionUpdateView.as_view()),
    path('api/exhibits/add/', views_api.ExhibitCreateAPIView.as_view()),
    path('api/exhibitions/add/', views_api.ExhibitionCreateAPIView.as_view()),
    path('api/exhibits/delete/<int:pk>/', views_api.ExhibitDeleteAPI.as_view()),
    path('api/exhibitions/delete/<int:pk>/', views_api.ExhibitionDeleteAPI.as_view()),
    path('api/rooms/<int:room_id>', views_api.MuseumRoomDetails.as_view(), name='room-details'),
    path('api/rooms/<int:room_id>/exhibits', views_api.ExhibitsByRoom.as_view(), name='exhibits-by-room'),
    path('api/rooms/add/', views_api.MuseumRoomCreateAPIView.as_view()),
    path('api/rooms/update/<int:pk>/', views_api.MuseumRoomUpdateView.as_view()),
    path('api/rooms/delete/<int:pk>/', views_api.MuseumRoomDeleteAPI.as_view())
]
