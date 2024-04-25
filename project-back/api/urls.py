from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from api.views import (get_aviatours, get_aviatour, get_hotels, get_hotel,
                       get_top_aviatours, ReservationsGeneric, ReservationDetailGeneric,
                       UserCreationGeneric, UnitUserGeneric, create_user, list_users)

urlpatterns = [
    #authentication urls
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),

    path('login/create/', create_user),
    path('login/list/', list_users),
    #tours' urls
    path('aviatours/', get_aviatours),
    path('aviatours/<int:pkey>/', get_aviatour),
    path('aviatours/top_ten/', get_top_aviatours),
    #reservations' urls
    path('reservations/', ReservationsGeneric.as_view()),
    path('reservations/<int:pkey>/', ReservationDetailGeneric.as_view()),
    #hotels' urls
    path('hotels/', get_hotels),
    path('hotels/<int:pkey>/', get_hotel),
    #users' urls
    path('users/<int:pk>/', UnitUserGeneric.as_view()),
    path('users/', UserCreationGeneric.as_view()),
]
