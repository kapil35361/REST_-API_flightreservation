from django.db import models

# Create your models here.

class Flight(models.Model):
    flightNumber=models.CharField(max_length=20)
    operatingAirlines=models.CharField(max_length=20)
    departureCity=models.CharField(max_length=20)
    ArrivalCity=models.CharField(max_length=20)
    dateofdeparture=models.DateField()
    estimatetime=models.TimeField()

    def __str__(self):
        return f'{self.flightNumber},{self.operatingAirlines},departurecity={self.departureCity},{self.ArrivalCity},{self.dateofdeparture},{self.estimatetime}'
    



class Passenger(models.Model):
    firstName=models.CharField(max_length=20)
    lastName=models.CharField(max_length=20)
    emailid=models.EmailField()
    phonenumber=models.CharField(max_length=12)


class Reservation(models.Model):
    passenger=models.ForeignKey(Passenger,related_name='Flight', on_delete=models.CASCADE)
    flight=models.ForeignKey(Flight,related_name='passenger',on_delete=models.CASCADE)

