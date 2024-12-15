from rest_framework import serializers

from .models import Exhibition, MuseumRoom


class ExhibitionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exhibition
        fields = ['name', 'start_date', 'end_date', 'country', 'city', 'venue', 'responsible_person', 'museum']

class MuseumRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = MuseumRoom
        fields = ['room_number', 'description', 'museum']