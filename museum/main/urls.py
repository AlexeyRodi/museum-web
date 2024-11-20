from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('комнаты/',views.rooms_list, name='rooms_list'),
    path('выставки/',views.exhibitons_list, name='exhibitions_list'),
    path('экспонаты/',views.exhibits_list, name='exhibits_list'),
]