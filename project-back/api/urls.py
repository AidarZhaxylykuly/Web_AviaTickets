from django.urls import path, re_path

from api.views import get_aviatours, get_aviatour, get_reservations, get_reservation, get_top_aivatours

urlpatterns = [
    path('aviatours/', get_aviatours),
    path('aviatours/<int:pkey>/', get_aviatour),
    path('reservations/', get_reservations),
    path('reservations/<int:pkey>/',get_reservation),
    path('aviatours/top_ten/', get_top_aivatours),
]
