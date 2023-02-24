from django.shortcuts import render
from rest_framework import viewsets,generics
from . models import *
from .serializers import *

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import filters
from django.db.models import Avg

# Create your views here.

class viewTourismPlace(viewsets.ModelViewSet):
    queryset = TourismPlace.objects.all()
    serializer_class = ToutismPlaceSerializer

    @action(detail=True, methods=['post'])
    def rate_TourismPlace(self, request, pk=None):
        if 'stars' in request.data:
            tourismPlace = TourismPlace.objects.get(id=pk)
            stars = request.data['stars']
            username = request.data['username']
            user = User.objects.get(id=username)
            # update:
            try:
                rating = RateTourismPlace.objects.get(user=username,tourismPlace=tourismPlace)
                rating.stars = stars
                rating.save()
                serializer = RateTourismPlaceSerializer(rating,many = False)
                json = {
                    'message': 'Tourism Place Rate Updated',
                    'result': serializer.data
                }
                return Response(json)
            # create:
            except:    
                rating = RateTourismPlace.objects.create(user=user,tourismPlace=tourismPlace,stars=stars)
                serializer = RateTourismPlaceSerializer(rating,many = False)
                json = {
                    'message': 'Tourism Place Rate Created',
                    'result': serializer.data
                }
                return Response(json)
        return Response("json")


class viewHotel(viewsets.ModelViewSet):

    search_fields = ['description','name']
    filter_backends = (filters.SearchFilter,filters.OrderingFilter)

    ordering_fields = ['name', 'address']

    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

    @action(detail=True, methods=['post'])
    def rate_Hotel(self, request, pk=None):
        if 'stars' in request.data:
            hotel = Hotel.objects.get(id=pk)
            stars = request.data['stars']
            username = request.data['username']
            user = User.objects.get(id=username)
            # update:
            try:
                rating = RateHotel.objects.get(user=username,hotel=hotel)
                rating.stars = stars
                rating.save()
                serializer = RateHotelSerializer(rating,many = False)
                json = {
                    'message': 'Hotel Rate Updated',
                    'result': serializer.data
                }
                return Response(json)
            # create:
            except:    
                rating = RateHotel.objects.create(user=user,hotel=hotel,stars=stars)
                serializer = RateHotelSerializer(rating,many = False)
                json = {
                    'message': 'Hotel Rate Created',
                    'result': serializer.data
                }
                return Response(json)
        return Response("json")
 
    @action(detail=False, methods=['Get'])
    def searchRateNamber(self, request):
        json = []
        json2 = []
        RateNamber = request.data['RateNamber']
        # print("RateNamber",RateNamber)
        for obj in Hotel.objects.all(): 
            # print(RateHotel.objects.filter(hotel=obj).aggregate(Avg('stars'))['stars__avg'])
            if RateHotel.objects.filter(hotel=obj).aggregate(Avg('stars'))['stars__avg'] == float(RateNamber):
                json.append(obj.id)
                # print(json)
        for i in range(len(json)):
            hotels_by_rateNamber = Hotel.objects.get(id = json[i])
            serializer = HotelSerializer(hotels_by_rateNamber)
            json2.append(serializer.data)
        return Response(json2) # , status=status.HTTP_200_OK

    

# class viewSearch(viewsets.ModelViewSet):
#     queryset = Hotel.objects.all()
#     serializer_class = HotelSerializer

    
    # @action(detail=False, methods=['Get'])
    # def search_Hotel(self, request):
    #     # rateNamber = request.data['Rate Namber']
    #     # hotel_of_rateNamber = Hotel.search(rateNamber)
    #     print("ayman",Hotel.objects.all())
    #     return Response("hotel_of_rateNamber")
    
# # Get all Hotels by Rate Namber
#     @action(detail=False, methods=['Get'])
#     def search(self, request):
#         json=[]
#         stars = request.data['stars']
#         rate = RateHotel.objects.filter(stars=stars).values()
#         for i in range(len(rate)):
#             hotels_by_rateNamber = Hotel.objects.get(id = rate[i]['hotel_id'])
#             serializer = HotelSerializer(hotels_by_rateNamber)
#             json.append(serializer.data)
#         return Response(json) # , status=status.HTTP_200_OK

    
    

class viewRateTourismPlace(viewsets.ModelViewSet):
    queryset = RateTourismPlace.objects.all()
    serializer_class = RateTourismPlaceSerializer

class viewRateHotel(viewsets.ModelViewSet):
    queryset = RateHotel.objects.all()
    serializer_class = RateHotelSerializer

