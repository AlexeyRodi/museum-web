from .models import Exhibition, MuseumRoom

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ExhibitionsSerializer, MuseumRoomSerializer


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
