from rest_framework import serializers

from api.models import AviaTour, Hotel, Reservation, UnitUser


class AviaSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    arrival_airport = serializers.CharField(max_length=100)
    city1 = serializers.CharField(max_length=100)
    city2 = serializers.CharField(max_length=100)
    cost = serializers.IntegerField()
    date_of_arrival = serializers.DateField()
    date_of_departure = serializers.DateField()
    duration_of_visit = serializers.IntegerField()
    pic_url = serializers.CharField(max_length=500)
    likes = serializers.IntegerField(default=0)

    def create(self, validated_data):
        instance = AviaTour.objects.create(
          name=validated_data.get("name"),
          description = validated_data.get("description"),
          arrival_airport = validated_data.get("arrival_airport"),
          city1 = validated_data.get("city1"),
          city2 = validated_data.get("city2"),
          cost = validated_data.get("cost"),
          date_of_arrival = validated_data.get("date_of_arrival"),
          date_of_departure = validated_data.get("date_of_departure"),
          duration_of_visit = validated_data.get("duration_of_visit"),
          pic_url = validated_data.get("pic_url"),
          likes = validated_data.get("likes")
        )
        return instance

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name")
        instance.description = validated_data.get("description")
        instance.arrival_airport = validated_data.get("arrival_airport")
        instance.city1 = validated_data.get("city1")
        instance.city2 = validated_data.get("city2")
        instance.cost = validated_data.get("cost")
        instance.date_of_arrival = validated_data.get("date_of_arrival")
        instance.date_of_departure = validated_data.get("date_of_departure")
        instance.duration_of_visit = validated_data.get("duration_of_visit")
        instance.pic_url = validated_data.get("pic_url")
        instance.likes = validated_data.get("likes")
        instance.save()
        return instance


class HotelSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=75)
    city = serializers.CharField(max_length=75)
    cost_per_person = serializers.IntegerField()
    stars = serializers.IntegerField()

    def create(self, validated_data):
        instance = Hotel.objects.create(
          name=validated_data.get("name"),
          city = validated_data.get("city"),
          cost_per_person = validated_data.get("cost_per_person"),
          stars = validated_data.get("stars")
        )
        return instance

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name"),
        instance.city = validated_data.get("city"),
        instance.cost_per_person = validated_data.get("cost_per_person"),
        instance.stars = validated_data.get("stars")
        instance.save()
        return instance


class UnitUserSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = UnitUser
        fields = ("user_id", "name", "surname", "email", "contacts")


class ReservationSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(read_only=True)
    class Meta:
        model = Reservation
        fields = ("unit_user", "num_of_people", "acceptance", "hotel", "aviatour", "total_cost", "user_id")
