from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from api.models import UnitUser, Reservation
from api.serializers import UnitUserSerializer, ReservationSerializer


class ReservationsGeneric(generics.ListCreateAPIView):
    serializer_class = ReservationSerializer
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ReservationDetailGeneric(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReservationSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Reservation.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserCreationGeneric(generics.CreateAPIView):
    queryset = UnitUser.objects.all()
    serializer_class = ReservationSerializer


class UnitUserGeneric(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UnitUserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return UnitUser.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
