import base64

from django.core.files.base import ContentFile
from django.core.serializers import serialize
from rest_framework import status
from rest_framework.generics import UpdateAPIView, ListCreateAPIView
from rest_framework.viewsets import ModelViewSet

from .models import Exhibition, MuseumRoom, Exhibit

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ExhibitionsSerializer, MuseumRoomSerializer, ExhibitSerializer
from django.shortcuts import get_object_or_404


class ExhibitionsAPI(APIView):
    def get(self, request):
        exhibitions = Exhibition.objects.all()
        serializer = ExhibitionsSerializer(exhibitions, many=True)
        return Response(serializer.data)


class MuseumRoomAPI(APIView):
    def get(self, request):
        museum_rooms = MuseumRoom.objects.all().order_by('room_number')
        serializer = MuseumRoomSerializer(museum_rooms, many=True)
        return Response(serializer.data)


class ExhibitAPI(APIView):
    def get(self, request):
        exhibits = Exhibit.objects.all()
        serializer = ExhibitSerializer(exhibits, many=True)
        return Response(serializer.data)


class ExhibitDetailAPI(APIView):
    def get(self, request, pk):
        exhibit = get_object_or_404(Exhibit, pk=pk)
        serializer = ExhibitSerializer(exhibit)
        return Response(serializer.data)


class ExhibitionDetailAPI(APIView):
    def get(self, request, pk):
        exhibition = get_object_or_404(Exhibition, pk=pk)
        serializer = ExhibitionsSerializer(exhibition)
        return Response(serializer.data)


class ExhibitUpdateView(UpdateAPIView):
    queryset = Exhibit.objects.all()
    serializer_class = ExhibitSerializer


class ExhibitionUpdateView(UpdateAPIView):
    queryset = Exhibition.objects.all()
    serializer_class = ExhibitionsSerializer


class MuseumRoomUpdateView(UpdateAPIView):
    queryset = MuseumRoom.objects.all()
    serializer_class = MuseumRoomSerializer


class ExhibitCreateAPIView(ListCreateAPIView):
    queryset = Exhibit.objects.all()
    serializer_class = ExhibitSerializer


class ExhibitionCreateAPIView(ListCreateAPIView):
    queryset = Exhibition.objects.all()
    serializer_class = ExhibitionsSerializer


class MuseumRoomCreateAPIView(ListCreateAPIView):
    queryset = MuseumRoom.objects.all()
    serializer_class = MuseumRoomSerializer


class ExhibitDeleteAPI(APIView):
    def delete(self, request, pk, format=None):
        try:
            exhibit = Exhibit.objects.get(pk=pk)
            exhibit.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exhibit.DoesNotExist:
            return Response({"error": "Exhibit not found"}, status=status.HTTP_404_NOT_FOUND)


class ExhibitionDeleteAPI(APIView):
    def delete(self, request, pk, format=None):
        try:
            exhibition = Exhibition.objects.get(pk=pk)
            exhibition.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exhibition.DoesNotExist:
            return Response({"error": "Exhibition not found"}, status=status.HTTP_404_NOT_FOUND)


class MuseumRoomDeleteAPI(APIView):
    def delete(self, request, pk, format=None):
        try:
            room = MuseumRoom.objects.get(pk=pk)
            room.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exhibition.DoesNotExist:
            return Response({"error": "Room not found"}, status=status.HTTP_404_NOT_FOUND)


class MuseumRoomDetails(APIView):
    def get(self, request, room_id):
        try:
            room = MuseumRoom.objects.get(room_id=room_id)
            serializer = MuseumRoomSerializer(room)
            return Response(serializer.data)
        except MuseumRoom.DoesNotExist:
            return Response(
                {"error": "Комната не найдена"}, status=status.HTTP_404_NOT_FOUND
            )


class ExhibitsByRoom(APIView):
    def get(self, request, room_id):
        try:
            room = MuseumRoom.objects.get(room_id=room_id)
            exhibits = room.exhibit_set.all()  # Используем related_name "exhibits"
            serializer = ExhibitSerializer(exhibits, many=True)
            return Response(serializer.data)
        except MuseumRoom.DoesNotExist:
            return Response(
                {"error": "Комната не найдена"}, status=status.HTTP_404_NOT_FOUND
            )
