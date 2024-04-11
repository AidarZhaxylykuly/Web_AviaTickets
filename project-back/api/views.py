import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api.models import AviaTour, Reservation


@csrf_exempt
def get_aviatours(request):
      tours = AviaTour.objects.all()
      tours_json = [tour.to_json() for tour in tours]
      return JsonResponse(tours_json, safe = False)


@csrf_exempt
def get_aviatour(request, pkey=None):
    try:
        aviatour = AviaTour.objects.get(id=pkey)
    except AviaTour.DoesNotExist as e:
        return JsonResponse({
            'error': str(e),
        }, status = 400)

    # actions according to the type of the request
    return JsonResponse(aviatour.to_json(), safe=False)


@csrf_exempt
def get_reservations(request):
    if request.method == 'GET':
        reservations = Reservation.objects.all()
        reservations_json = [reservation.to_json() for reservation in reservations]
        return JsonResponse(reservations_json, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        reservation = AviaTour.objects.create( name = data.get("name"), surname = data.get("surname"), email = data.get("email"), contacts = data.get("contacts"), num_of_people = data.get("num_of_people"), acceptance = data.get("acceptance"), aviatour = data.get("aviatour"))
        return JsonResponse(reservation.to_json(), safe=False)


@csrf_exempt
def get_reservation(request, pkey=None):
    try:
        reservation = Reservation.objects.get(id = pkey)
    except Reservation.DoesNotExist as e:
        return JsonResponse({
            'error': str(e)
        }, status = 400)

    # actions according to the type of the request
    if request.method == "GET":
        return JsonResponse(reservation.to_json(), safe=False)

    # pay attention, that we could change only basic data info, like name, surname, contacts
    elif request.method == "PUT":
        data = json.loads(request.body)
        reservation.name = data.get("name")
        reservation.surname = data.get("surname")
        reservation.contacts = data.get("contacts")
        reservation.save()
        return JsonResponse(reservation.to_json(), safe=False)
    elif request.method == "DELETE":
        reservation.delete()
        return JsonResponse({"deleted": True})


def get_top_aivatours(request):
    aviatours = AviaTour.objects.filter().order_by("likes")[:5]
    aviatours_json = [aviatour.to_json() for aviatour in aviatours]
    return JsonResponse(aviatours_json, safe=False)
