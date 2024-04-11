from django.db import models

# Create your models here.

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
    likes = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Avia tour"
        verbose_name_plural = 'Avia tours'

    def __str__(self):
        return f'Id: {self.id}, Name: {self.name}, Description: {self.description}, Departure_Airport: {self.arrival_airport}, City_1: {self.city1}, City_2: {self.city2}, Cost: {self.cost}, Arrival_Date: {self.date_of_arrival}, Departure_Date: {self.date_of_departure}, Duration: {self.duration_of_visit}, Likes: {self.likes}'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'city_1': self.city1,
            'city_2': self.city2,
            'cost': self.date_of_arrival,
            'date_of_arrival': self.date_of_arrival,
            'date_of_departure': self.date_of_departure,
            'duration_of_visit': self.duration_of_visit,
            'likes': self.likes
        }

class Reservation(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contacts = models.CharField(max_length=12)
    num_of_people = models.IntegerField()
    acceptance = models.BooleanField(default=False)
    aviatour = models.ForeignKey(
        AviaTour,
        on_delete = models.PROTECT,
        related_name= "reservations"
    )
    total_cost = models.BooleanField()

    class Meta:
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'


    def __str__(self):
        return f'Id: {self.id}, Name: {self.name}, Surname: {self.surname}, Email: {self.email}, Contants:{self.contacts}, PeopleNumber: {self.num_of_people}, Acceptance: {self.acceptance}, Aviatour: {self.aviatour.id}'

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'email': self.contacts,
            'contacts': self.contacts,
            'num_of_people': self.num_of_people,
            'acceptance': self.acceptance,
            'aviatour': self.aviatour
        }
