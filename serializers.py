from rest_framework import serializers
from .models import Band, Venue


class BandSerializer(serializers.ModelSerializer):
    genre = serializers.ChoiceField(choices=Band.GENRE_CHOICES)

    class Meta:
        model = Band
        fields = ['id', 'band_name', 'email', 'username',
                  'password', 'genre']


class VenueSerializer(serializers.ModelSerializer):
    type_of_music = serializers.ChoiceField(choices=Venue.MUSIC_TYPES)

    class Meta:
        model = Venue
        fields = ['id', 'venue_name', 'email', 'username',
                  'password', 'type_of_music']
