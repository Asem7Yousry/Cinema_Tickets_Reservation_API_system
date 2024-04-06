from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

#### model for movie object ####
class Movie(models.Model):
    title = models.CharField(max_length = 30)
    hall = models.CharField(max_length = 30)
    duration = models.FloatField()

    ### function to show instance with its name ###
    def __str__(self):
        return f'{self.title}'

#### guest model ####
class Guest(models.Model):
    name = models.CharField(max_length = 30)
    phone_number = PhoneNumberField()

    ### function to show instance with its name ###
    def __str__(self):
        return f'{self.name}'

### starting hours for movie sessions ###
session_hour = (
    ('12-pm','12-pm'),
    ('3-pm','3-pm'),
    ('6-pm','6-pm'),
    ('9-pm','9-pm'),
    ('12-am','12-am'),
)

##### Reservation model object #####
class Reservation(models.Model):
    guest_name = models.ForeignKey(Guest , on_delete= models.CASCADE , related_name='reservation')
    movie_name = models.ForeignKey(Movie , on_delete= models.CASCADE , related_name='reservation')
    date = models.DateField(auto_now= True )
    time = models.CharField(max_length= 5 , choices= session_hour )
    price = models.FloatField()

    ### function to show instance with its name ###
    def __str__(self):
        return f'{self.guest_name}'
    
