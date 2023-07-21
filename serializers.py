from rest_framework import serializers
from django import forms
from .models import Artist, Unavailability, Venue, ArtistListedGig, VenueListedGig, NewsletterSignup, MembershipOptions, ArtistWrittenReview, VenueWrittenReview, GigApplication
from .choices import UK_COUNTY_CHOICES


class ArtistSerializer(serializers.ModelSerializer):
    gigging_distance = serializers.MultipleChoiceField(
        choices=UK_COUNTY_CHOICES, required=False)

    class Meta:
        model = Artist
        fields = ['id', 'artist_name', 'email', 'password', 'phone_number', 'bio', 'summary', 'genre',
                  'country', 'county', 'type_of_artist', 'image', 'featured_artist', 'facebook', 'twitter', 'youtube', 'artist_membership_type', 'gigging_distance']


class UnavailabilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Unavailability
        fields = ['id', 'artist', 'date']


class VenueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Venue
        fields = ['id', 'venue_name', 'email', 'password', 'phone_number', 'bio',
                  'country', 'county', 'image', 'type_of_act', 'facebook', 'twitter', 'youtube', 'venue_membership_type']


class ArtistListedGigSerializer(serializers.ModelSerializer):
    artist_name = serializers.CharField(
        source='artist.artist_name', read_only=True)

    class Meta:
        model = ArtistListedGig
        fields = ['id', 'artist_name', 'date_of_gig', 'venue_name',
                  'country_of_venue', 'genre_of_gig', 'type_of_gig', 'artist_type', 'payment', 'user_type']


class VenueListedGigSerializer(serializers.ModelSerializer):
    venue = serializers.CharField(source='venue.venue_name')

    class Meta:
        model = VenueListedGig
        fields = ['id', 'venue', 'date_of_gig',
                  'country_of_venue', 'genre_of_gig', 'type_of_gig', 'artist_type', 'payment', 'user_type']


class NewsletterSignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = NewsletterSignup
        fields = ['id', 'email']


class MembershipOptionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = MembershipOptions
        fields = ['id', 'membership_id', 'type_of_user', 'title', 'description',
                  'price', 'disclosure', 'is_active']


class ArtistWrittenReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = ArtistWrittenReview
        fields = ['id', 'date_of_performance',
                  'artist_name', 'venue_name', 'review', 'rating', 'is_approved']


class VenueWrittenReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = VenueWrittenReview
        fields = ['id', 'date_of_performance',
                  'venue_name', 'artist_name', 'review', 'rating', 'is_approved']


class GigApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = GigApplication
        fields = ['id', 'artist_name', 'email']
