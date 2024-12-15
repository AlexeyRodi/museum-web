from rest_framework import serializers

from .models import Exhibition


class ExhibitionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exhibition
        fields = ['name', 'start_date', 'end_date', 'country', 'city', 'venue', 'responsible_person', 'museum']
