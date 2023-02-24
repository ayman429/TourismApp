from rest_framework import serializers
from .models import *


class ToutismPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TourismPlace
        fields = ('name', 'image', 'description', 'address','no_of_ratings','avg_ratings','rate_one_by_one')

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('name', 'image', 'description', 'address','no_of_ratings','avg_ratings','rate_one_by_one')    



class RateTourismPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = RateTourismPlace
        fields = '__all__'

class RateHotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = RateHotel
        fields = '__all__'


    


   
