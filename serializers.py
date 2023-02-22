from rest_framework import serializers
from .models import Band, Venue


class BandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Band
        fields = ['id', 'band_name', 'email', 'username',
                  'password', 'genre']


class VenueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields = ['id', 'venue_name', 'email', 'username',
                  'password', 'type_of_music']
