from django.db import models
from django.contrib.auth.models import User


class AviaTour(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    arrival_airport = models.CharField(max_length=100)
    city1 = models.CharField(max_length=100)
    city2 = models.CharField(max_length=100)
    cost = models.IntegerField()
    date_of_arrival = models.DateField()
    date_of_departure = models.DateField()
    duration_of_visit = models.IntegerField()
    pic_url = models.CharField(max_length=500)
    likes = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Avia tour"
        verbose_name_plural = 'Avia tours'

    def __str__(self):
        return f'Id: {self.id}, Name: {self.name}, Description: {self.description}, Departure_Airport: {self.arrival_airport}, City_1: {self.city1}, City_2: {self.city2}, Cost: {self.cost}, Arrival_Date: {self.date_of_arrival}, Departure_Date: {self.date_of_departure}, Duration: {self.duration_of_visit}, PictureURL: {self.pic_url}, Likes: {self.likes}'


class Hotel(models.Model):
  name = models.CharField(max_length=75)
  city = models.CharField(max_length=75)
  cost_per_person = models.IntegerField()
  stars = models.IntegerField()

  class Meta:
    verbose_name = 'Hotel'
    verbose_name_plural = 'Hotels'

  def __str__(self):
    return f'Id: {self.id}, Name: {self.name}, City: {self.cost_per_person}, Stars: {self.stars}'


class UnitUser(models.Model):
  user = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    related_name="unit_user",
    null=True,
    blank=True
  )
  name = models.CharField(max_length=100)
  surname = models.CharField(max_length=100)
  email = models.CharField(max_length=100)
  contacts = models.CharField(max_length=12)

  class Meta:
    verbose_name = "Unit_User"
    verbose_name_plural = "Unit_Users"

  def __str__(self):
    return f'Id: {self.id}, Name: {self.name}, Surname: {self.surname}, Email: {self.email}, Contants:{self.contacts}'


class Reservation(models.Model):
    user = models.ForeignKey(
      User,
      on_delete=models.CASCADE,
      related_name="reservations",
      null=True,
      blank=True
    )
    unit_user = models.ForeignKey(
      UnitUser,
      on_delete=models.CASCADE,
      related_name="reservations"
    )
    num_of_people = models.IntegerField()
    acceptance = models.BooleanField(default=False)
    hotel = models.ForeignKey(
      Hotel,
      on_delete=models.PROTECT,
      related_name="reservations"
    )
    aviatour = models.ForeignKey(
        AviaTour,
        on_delete=models.PROTECT,
        related_name="reservations"
    )
    total_cost = models.IntegerField()

    class Meta:
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'

    def __str__(self):
        return f'User: {self.unit_user}, PeopleNumber: {self.num_of_people}, Acceptance: {self.acceptance},Hotel: {self.hotel}, Aviatour: {self.aviatour.id}, TotalCost: {self.total_cost}'
