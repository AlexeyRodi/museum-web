from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('комнаты/', views.rooms_list, name='rooms_list'),
    path('выставки/', views.exhibitons_list, name='exhibitions_list'),
    path('экспонаты/', views.exhibits_list, name='exhibits_list'),
    path('exhibits/<int:room_id>/', views.exhibits_list, name='exhibits_list'),
    path('добавитьвыставку/', views.add_exhibition, name='add_exhibition'),
    path('добавитькомнату/', views.add_museum_room, name='add_museum_room'),
    path('<int:pk>/изменитьвыставку/',views.ExhibitionUpdateView.as_view(), name='update_exhibition'),
    path('<int:pk>/изменитькомнатумузея/',views.MuseumRoomUpdateView.as_view(), name='update_museum_room')
]
