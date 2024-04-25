from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from api.models import AviaTour, Hotel
from api.serializers import AviaSerializer, HotelSerializer

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.http import JsonResponse
import json


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

#users' views

@csrf_exempt
def create_user(request):
  if request.method == 'POST':
    try:
      data = json.loads(request.body)
      username = data.get('username')
      password = data.get('password')
      email = data.get('email')

      if not username or not password or not email:
        return JsonResponse({'error': 'All fields are required'}, status=400)

      user = User.objects.create_user(username=username, password=password, email=email)

      return JsonResponse({'message': 'User created successfully'}, status=201)
    except Exception as e:
      return JsonResponse({'error': str(e)}, status=500)
  else:
    return JsonResponse({'error': 'Only POST method allowed'}, status=405)


def list_users(request):
  users = User.objects.all()
  user_data = [{'id': user.id, 'username': user.username} for user in users]
  return JsonResponse({'users': user_data})
