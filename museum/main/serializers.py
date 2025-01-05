from rest_framework import serializers

from .models import Exhibition, MuseumRoom, Exhibit


class ExhibitionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exhibition
        fields = ['name', 'start_date', 'end_date', 'country', 'city', 'venue', 'responsible_person', 'museum']


class MuseumRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = MuseumRoom
        fields = ['room_number', 'description', 'museum']


class ExhibitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exhibit
        fields = ['exhibit_id','name', 'description', 'creation_year', 'creator', 'room', 'image']
