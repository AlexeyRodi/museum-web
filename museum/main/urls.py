from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('комнаты/',views.rooms_list, name='rooms_list'),
]