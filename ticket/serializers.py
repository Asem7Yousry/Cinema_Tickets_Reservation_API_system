from rest_framework import serializers
from .models import Guest , Movie , Reservation

#### serializer object for guest ####
class Guest_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Guest
        fields = '__all__'

#### serializer object for movie ####
class Movie_Serializer(serializers.ModelSerializer):
    class Meta:     
        model = Movie
        fields = '__all__'

#### serializer object for Reservation ####
class Reservation_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'





