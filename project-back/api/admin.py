from django.contrib import admin

from api.models import AviaTour, Reservation, Hotel, UnitUser


# Register your models here.


@admin.register(UnitUser)
class UnitUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'surname', 'email', 'contacts')
    search_fields = ('email', 'name')


@admin.register(AviaTour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'city1', 'city2', 'cost', 'date_of_arrival',
                    'date_of_departure', 'duration_of_visit', 'pic_url', 'likes')
    search_fields = ('name',)


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'unit_user', 'num_of_people',
                    'acceptance', 'hotel', 'aviatour', 'total_cost', 'user')
    search_fields = ('name', 'company',)

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city', 'cost_per_person', 'stars')
    search_fields = ('name', 'stars',)
