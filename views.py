from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Band, Availability, Venue, ArtistListedGig
from .serializers import BandSerializer, AvailabilitySerializer, VenueSerializer, ArtistListedGigSerializer


# Band View

@api_view(['GET', 'POST'])
def band_list(request, format=None):

    if request.method == 'GET':
        bands = Band.objects.all()
        serializer = BandSerializer(bands, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BandSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def band_detail(request, id, format=None):

    try:
        band = Band.objects.get(pk=id)
    except Band.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BandSerializer(band)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BandSerializer(band, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        band.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Availability View

@api_view(['GET', 'POST'])
def availability_list(request, format=None):

    if request.method == 'GET':
        availabilities = Availability.objects.all()
        serializer = AvailabilitySerializer(availabilities, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AvailabilitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def availability_detail(request, id, format=None):
    try:
        availability = Availability.objects.filter(band_id=id)
    except Availability.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = AvailabilitySerializer(availability, many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = AvailabilitySerializer(availability, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        availability.delete()
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


# VALIDATE BAND USER VIEW

@api_view(['POST'])
def band_sign_in(request):
    email = request.data.get('email')
    password = request.data.get('password')

    band = get_object_or_404(Band, email=email, password=password)
    serializer = BandSerializer(band)

    return Response({'id': band.id})


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
