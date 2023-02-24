from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('TourismPlace',viewTourismPlace)
router.register('Hotel',viewHotel)
router.register('RateTourismPlace',viewRateTourismPlace)
router.register('RateHotel',viewRateHotel)
# router.register('search_Hotel',viewSearch)

urlpatterns = [
    path('', include(router.urls)),
]