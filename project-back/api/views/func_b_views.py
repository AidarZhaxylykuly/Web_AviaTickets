from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework import status

from api.models import AviaTour, Reservation

from rest_framework.request import Request
from rest_framework.response import Response

from api.serializers import AviaSerializer, ReservationSerializer


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


@api_view(["GET", "POST"])
def get_reservations(request):
  if request.method == 'GET':
    reservations = Reservation.objects.all()
    serialized_reservations = ReservationSerializer(reservations, many=True)
    return Response(serialized_reservations.data)
  elif request.method == 'POST':
    serializer = ReservationSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def get_reservation(request, pkey=None):
  try:
    reservation = Reservation.objects.get(id=pkey)
  except Reservation.DoesNotExist as e:
    return Response({
      'error': str(e)
    }, status=400)

  # actions according to the type of the request
  if request.method == "GET":
    serializer = ReservationSerializer(reservation)
    return Response(serializer.data)
  elif request.method == "PUT":
    serializer = ReservationSerializer(
      instance=reservation,
      data=request.data
    )
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  elif request.method == "DELETE":
    reservation.delete()
    return JsonResponse({"deleted": True})

@api_view(["GET"])
def get_top_aviatours(request):
  tours = AviaTour.objects.filter().order_by("-likes")[:5]
  serializer_list = AviaSerializer(tours, many=True)
  return Response(serializer_list.data)
