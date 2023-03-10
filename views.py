from .models import Band, Venue
from .serializers import BandSerializer, VenueSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


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
