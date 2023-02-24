from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth.models import User
# Create your models here.

###########################################
# Tourism Place:                          #
# --> name, image, description, address   #
###########################################
class TourismPlace(models.Model):
    name = models.CharField(max_length=100,unique=True)
    image = models.ImageField(upload_to='photo/%y/%m/%d')
    description = models.TextField()
    address = models.CharField(max_length=100)

    def no_of_ratings(self):
        ratings = RateTourismPlace.objects.filter(tourismPlace=self)
        return len(ratings)

    def avg_ratings(self):
        ratings = RateTourismPlace.objects.filter(tourismPlace=self)
        length = len(ratings)
        sum = 0
        for i in ratings:
            sum += i.stars
        if length!=0:
            avg = sum / length
        else:
            avg=0
        return avg
    
    def rate_one_by_one(self):
        rate1=0
        rate2=0
        rate3=0
        rate4=0
        rate5=0
        ratings = RateTourismPlace.objects.filter(tourismPlace=self)
        length = len(ratings)
        for i in ratings:
            if i.stars == 1:
                rate1+=1
            elif i.stars == 2:
                rate2+=1
            elif i.stars == 3:
                rate3+=1
            elif i.stars == 4:
                rate4+=1
            elif i.stars == 5:
                rate5+=1
        
        if length !=0:
            val1 = int((rate1/length)*100)
            val2 = int((rate2/length)*100)
            val3 = int((rate3/length)*100)
            val4 = int((rate4/length)*100)
            val5 = int((rate5/length)*100)
        else:  
            val1 = 0 ; val2 = 0 ; val3 = 0 ; val4 = 0 ; val5 = 0   

        list_of_rate = {"1":val1,"2":val2,"3":val3,"4":val4,"5":val5}

        return list_of_rate

    def __str__(self):
        return self.name

###########################################
# Hotel:                                  #
# --> name, image, description, address   #
###########################################


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photo/%y/%m/%d')
    description = models.TextField()
    address = models.CharField(max_length=100)
    # avg = models.DecimalField(max_digits=100,decimal_places=2,default=0)
    

    def no_of_ratings(self):
        ratings = RateHotel.objects.filter(hotel=self)
        return len(ratings)

    def avg_ratings(self):
        ratings = RateHotel.objects.filter(hotel=self)
        length = len(ratings)
        sum = 0
        for i in ratings:
            sum += i.stars
        if length!=0:
            avg = sum / length
        else:
            avg=0
        
        return avg
    
    def rate_one_by_one(self):
        rate1=0
        rate2=0
        rate3=0
        rate4=0
        rate5=0
        ratings = RateHotel.objects.filter(hotel=self)
        length = len(ratings)
        for i in ratings:
            if i.stars == 1:
                rate1+=1
            elif i.stars == 2:
                rate2+=1
            elif i.stars == 3:
                rate3+=1
            elif i.stars == 4:
                rate4+=1
            elif i.stars == 5:
                rate5+=1

        if length !=0:
            val1 = int((rate1/length)*100)
            val2 = int((rate2/length)*100)
            val3 = int((rate3/length)*100)
            val4 = int((rate4/length)*100)
            val5 = int((rate5/length)*100)

        else:  
            val1 = 0 ; val2 = 0 ; val3 = 0 ; val4 = 0 ; val5 = 0   

        list_of_rate = {"1":val1,"2":val2,"3":val3,"4":val4,"5":val5}
        return list_of_rate

    # avg = property(avg_ratings)
    # def search(self):
    #     hotel = Hotel.avg_ratings(self)
    #     print("hotel:",hotel)
    #     return hotel

    def __str__(self):
        return self.name

###########################################
# RateTourism Place:                      #
# --> tourismPlace, user, stars           #
###########################################
class RateTourismPlace(models.Model):
    tourismPlace = models.ForeignKey(TourismPlace,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    stars = models.PositiveSmallIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])


    class Meta:
        unique_together = (('user', 'tourismPlace'),)
        index_together = (('user', 'tourismPlace'),)

###########################################
# Rate Hotel:                             #
# --> TourismPlace, user, stars           #
###########################################
class RateHotel(models.Model):
    hotel = models.ForeignKey(Hotel,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    stars = models.PositiveSmallIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])

    class Meta:
        unique_together = (('user', 'hotel'),)
        index_together = (('user', 'hotel'),)

