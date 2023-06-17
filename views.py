from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Artist, Unavailability, Venue, ArtistListedGig, VenueListedGig, NewsletterSignup, MembershipOptions
from .serializers import ArtistSerializer, UnavailabilitySerializer, VenueSerializer, ArtistListedGigSerializer,  VenueListedGigSerializer, NewsletterSignupSerializer, MembershipOptionsSerializer
from django.db.models import Q
import json


# Artist View

@api_view(['GET', 'POST'])
def artist_list(request, format=None):

    if request.method == 'GET':
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArtistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def artist_detail(request, id, format=None):

    try:
        artist = Artist.objects.get(pk=id)
    except Artist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArtistSerializer(artist)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArtistSerializer(artist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        artist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Unavailability View

@api_view(['GET', 'POST'])
def unavailability_list(request, format=None):

    if request.method == 'GET':
        unavailabilities = Unavailability.objects.all()
        serializer = UnavailabilitySerializer(unavailabilities, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UnavailabilitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def unavailability_detail(request, id, format=None):

    try:
        unavailability = Unavailability.objects.filter(artist_id=id)
    except Unavailability.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UnavailabilitySerializer(unavailability, many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UnavailabilitySerializer(
            unavailability, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        unavailability.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Venue View

@api_view(['GET', 'POST'])
def venue_list(request, format=None):

    if request.method == 'GET':
        venues = Venue.objects.all()
        serializer = VenueSerializer(venues, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = VenueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def venue_detail(request, id, format=None):

    try:
        venue = Venue.objects.get(pk=id)
    except Venue.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VenueSerializer(venue)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = VenueSerializer(venue, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        venue.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# VALIDATE ARTIST USER VIEW

@api_view(['POST'])
def artist_sign_in(request):
    email = request.data.get('email')
    password = request.data.get('password')

    artist = get_object_or_404(Artist, email=email, password=password)
    serializer = ArtistSerializer(artist)

    return Response({'id': artist.id})


# VALIDATE VENUE USER VIEW

@api_view(['POST'])
def venue_sign_in(request):
    email = request.data.get('email')
    password = request.data.get('password')

    venue = get_object_or_404(Venue, email=email, password=password)
    serializer = VenueSerializer(venue)

    return Response({'id': venue.id})


# ArtistListedGig VIEW

@api_view(['GET', 'POST'])
def artist_listed_gig_list(request, format=None):

    if request.method == 'GET':
        artist_listed_gigs = ArtistListedGig.objects.all()
        serializer = ArtistListedGigSerializer(artist_listed_gigs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArtistListedGigSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def artist_listed_gig_detail(request, id, format=None):

    try:
        artist_listed_gig = ArtistListedGig.objects.get(pk=id)
    except ArtistListedGig.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArtistListedGigSerializer(artist_listed_gig)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArtistListedGigSerializer(
            artist_listed_gig, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        artist_listed_gig.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# VenueListedGig VIEW

@api_view(['GET', 'POST'])
def venue_listed_gig_list(request, format=None):

    if request.method == 'GET':
        venue_listed_gigs = VenueListedGig.objects.all()
        serializer = VenueListedGigSerializer(venue_listed_gigs, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = VenueListedGigSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def venue_listed_gig_detail(request, id, format=None):

    try:
        venue_listed_gig = VenueListedGig.objects.get(pk=id)
    except VenueListedGig.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VenueListedGigSerializer(venue_listed_gig)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = VenueListedGigSerializer(
            venue_listed_gig, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        venue_listed_gig.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# SEARCH FOR ARTISTS VIEW

@api_view(['POST'])
def artist_search(request):

    date_of_gig = request.data.get('date_of_gig')
    genre = request.data.get('genre')
    type_of_artist = request.data.get('type_of_artist')
    country = request.data.get('country')

    result = list(Artist.objects.filter(
        ~Q(unavailabilities__date=date_of_gig),
        genre=genre,
        type_of_artist=type_of_artist,
        country=country
    ).values())

    json_result = json.dumps(result)

    return Response(result)


# NewsletterSignup View

@api_view(['GET', 'POST'])
def newsletter_signup_list(request, format=None):

    if request.method == 'GET':
        newsletter_signups = NewsletterSignup.objects.all()
        serializer = NewsletterSignupSerializer(newsletter_signups, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = NewsletterSignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def newsletter_signup_detail(request, id, format=None):

    try:
        newsletter_signup = NewsletterSignup.objects.get(pk=id)
    except NewsletterSignup.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = NewsletterSignupSerializer(newsletter_signup)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = NewsletterSignupSerializer(
            newsletter_signup, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        newsletter_signup.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Featured Artist View

@api_view(['GET'])
def featured_artist_list(request, format=None):
    featured_artist = Artist.objects.filter(featured_artist=True)
    serializer = ArtistSerializer(featured_artist, many=True)
    return Response(serializer.data)


# Membership Options View

@api_view(['GET', 'POST'])
def membership_option_list(request, format=None):

    if request.method == 'GET':
        membership_options = MembershipOptions.objects.all()
        serializer = MembershipOptionsSerializer(membership_options, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = MembershipOptionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def membership_option_detail(request, id, format=None):

    try:
        membership_option = MembershipOptions.objects.get(pk=id)
    except MembershipOptions.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MembershipOptionsSerializer(membership_option)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MembershipOptionsSerializer(
            membership_option, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        membership_option.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# # Artist Listed Gig Search View

# @api_view(['POST'])
# def artist_listed_gig_search(request):

#     date_of_gig = request.data.get('date_of_gig')
#     country_of_venue = request.data.get('country_of_venue')
#     genre_of_gig = request.data.get('genre_of_gig')
#     type_of_gig = request.data.get('type_of_gig')
#     artist_type = request.data.get('artist_type')
#     payment = request.data.get('payment')

#     result = ArtistListedGig.objects.filter(
#         date_of_gig=date_of_gig, country_of_venue=country_of_venue, genre_of_gig=genre_of_gig, type_of_gig=type_of_gig, artist_type=artist_type, payment=payment)
#     serializer = ArtistListedGigSerializer(result, many=True)
#     return Response(serializer.data)


# # Venue Listed Gig Search View

# @api_view(['POST'])
# def venue_listed_gig_search(request):

#     date_of_gig = request.data.get('date_of_gig')
#     country_of_venue = request.data.get('country_of_venue')
#     genre_of_gig = request.data.get('genre_of_gig')
#     type_of_gig = request.data.get('type_of_gig')
#     artist_type = request.data.get('artist_type')
#     payment = request.data.get('payment')

#     result = VenueListedGig.objects.filter(
#         date_of_gig=date_of_gig, country_of_venue=country_of_venue, genre_of_gig=genre_of_gig, type_of_gig=type_of_gig, artist_type=artist_type, payment=payment)
#     serializer = VenueListedGigSerializer(result, many=True)
#     return Response(serializer.data)


# Gig Search View

@api_view(['POST'])
def gig_search(request):
    date_of_gig = request.data.get('date_of_gig')
    country_of_venue = request.data.get('country_of_venue')
    genre_of_gig = request.data.get('genre_of_gig')
    type_of_gig = request.data.get('type_of_gig')
    payment = request.data.get('payment')

    artist_listed_gigs = ArtistListedGig.objects.filter(
        date_of_gig=date_of_gig, country_of_venue=country_of_venue, genre_of_gig=genre_of_gig, type_of_gig=type_of_gig, payment__gte=payment)

    venue_listed_gigs = VenueListedGig.objects.filter(
        date_of_gig=date_of_gig, country_of_venue=country_of_venue, genre_of_gig=genre_of_gig, type_of_gig=type_of_gig, payment__gte=payment)

    artist_listed_gig_serializer = ArtistListedGigSerializer(
        artist_listed_gigs, many=True)
    venue_listed_gig_serializer = VenueListedGigSerializer(
        venue_listed_gigs, many=True)

    response_data = {
        'artist_listed_gigs': artist_listed_gig_serializer.data,
        'venue_listed_gigs': venue_listed_gig_serializer.data
    }

    return Response(response_data)
