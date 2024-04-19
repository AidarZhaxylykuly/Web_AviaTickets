from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from api.models import AviaTour, Hotel
from api.serializers import AviaSerializer, HotelSerializer


#tours' views

@api_view(["GET", "POST"])
def get_aviatours(request):
    if request.method == 'GET':
      tours = AviaTour.objects.all()
      serialized_tours = AviaSerializer(tours, many=True)
      return Response(serialized_tours.data)
    elif request.method == 'POST':
      serializer = AviaSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def get_aviatour(request, pkey=None):
  try:
    tour = AviaTour.objects.get(id=pkey)
  except AviaTour.DoesNotExist as e:
    return Response({
      'error': str(e),
    }, status=status.HTTP_400_BAD_REQUEST)

  # actions according to the type of the request
  if request.method == "GET":
    serializer = AviaSerializer(tour)
    return Response(serializer.data)
  elif request.method == "PUT":
    serializer = AviaSerializer(
      instance=tour,
      data=request.data
    )
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  elif request.method == "DELETE":
    tour.delete()
    return Response({"deleted": True})


def get_top_aviatours(request):
  tours = AviaTour.objects.filter().order_by("-likes")[:5]
  serializer_list = AviaSerializer(tours, many=True)
  return Response(serializer_list.data)


#hotels' views

@api_view(["GET", "POST"])
def get_hotels(request):
  if request.method == 'GET':
    hotels = Hotel.objects.all()
    serialized_hotels = HotelSerializer(hotels, many=True)
    return Response(serialized_hotels.data)
  elif request.method == 'POST':
    serializer = HotelSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_hotel(request, pkey=None):
  try:
    hotel = Hotel.objects.get(id=pkey)
    serializer = HotelSerializer(hotel)
    return Response(serializer.data)
  except Hotel.DoesNotExist as e:
    return Response({
      'error': str(e)
    }, status=400)
