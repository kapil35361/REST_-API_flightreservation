from flightapp.models import Flight,Passenger,Reservation
from flightapp.serializers import FlightSerializer,PassengerSerializer,ReservationSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django_filters.rest_framework import DjangoFilterBackend

@api_view(['POST'])
def FindfFlight(request):
    flight=Flight.objects.filter(departurecity=request.data('departurecity'),arrivalcity=request.data('arrivalcity'),dateofdeparture=request.data('dateofdeparture'))
    serializer=FlightSerializer(flight,many=True)
    return Response(serializer.data)


class PassengerViewset(viewsets.ModelViewSet):
    queryset=Passenger.objects.all()
    serializer_class=PassengerSerializer


class FlightViewset(viewsets.ModelViewSet):
    queryset=Flight.objects.all()
    serializer_class=FlightSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields=['departureCity','ArrivalCity','dateofdeparture']


class ReservationViewset(viewsets.ModelViewSet):
    queryset=Reservation.objects.all()
    serializer_class=ReservationSerializer


