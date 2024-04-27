from django.contrib import admin
from .models import Movie , Guest , Reservation

class MovieAdmin(admin.ModelAdmin):
    list_display = ['title','hall','duration']

class ReservationAdmin(admin.ModelAdmin):
    list_display = ['guest_name','movie_name','date','price']

admin.site.register(Movie , MovieAdmin)
admin.site.register(Guest)
admin.site.register(Reservation , ReservationAdmin)
