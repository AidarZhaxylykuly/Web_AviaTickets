from rest_framework import mixins, generics

from api.models import Hotel
from api.serializers import HotelSerializer


class HotelListMixin(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)
