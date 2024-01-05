from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.  

class Flight_Letter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return f"{self.email}"

    




class Airline(models.Model):
    name = models.CharField(max_length=200)
    airline_logoText = models.TextField()
    model = models.CharField(max_length=200, null=True)
    seat_numbers = models.PositiveIntegerField(default=0, null=True)
    # airline_logo = models.ImageField(upload_to='flight', default=0, null=True, blank=True)

    def __str__(self):
        return f"{self.name}: {self.seat_numbers}"


class Trip_Round(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.title}"


class Flight_Class(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return f"{self.name}"


class Offer(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True, default="default")

    def __str__(self):
        return f"{self.name}"
        
        
class Location(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class Booking(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    round = models.ForeignKey(Trip_Round, on_delete=models.CASCADE)
    flight_class = models.ForeignKey(Flight_Class, on_delete=models.CASCADE, default=None)
    offer = models.ForeignKey(Offer, on_delete=models.CASCADE, default=None)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE, default=None)

    depart_from = models.ForeignKey(Location, on_delete=models.CASCADE, default=None, related_name="booking_depart_from")
    destination = models.ForeignKey(Location, on_delete=models.CASCADE, default=None, related_name="booking_destination")
    departure = models.DateTimeField(default=None)
    arrival = models.DateTimeField(default=None)
    departure_2 = models.DateTimeField(default=None, null=True, blank=True)
    arrival_2 = models.DateTimeField(default=None, null=True, blank=True)
    passenger = models.CharField(default=1)
  
    stops = models.PositiveIntegerField(default=0)
    each_extra_luggage_price = models.DecimalField(decimal_places=2, max_digits=20, default=0)
    price = models.DecimalField(decimal_places=2, max_digits=20, default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.airline.name} > {self.depart_from} - {self.destination}: {self.departure} - {self.flight_class.name}: {self.round.title}"
    



class Hotel(models.Model):
    name = models.CharField()
    hotel_viewText = models.TextField()
    # hotel_view = models.ImageField(upload_to='hotel')

    def __str__(self):
        return f"{self.name}"
    

class City(models.Model):
    name = models.CharField(default=None)

    def __str__(self):
        return f"{self.name}"
       

class Conditions(models.Model):
    name = models.CharField()

    def __str__(self):
        return f"{self.name}"
    

class Rooms(models.Model):
    number = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.number}"
    

class HotelBooking(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, default=None, related_name="hotel_booking")
    city = models.ForeignKey(City, on_delete=models.CASCADE, default=None, related_name="hotel_booking_city")
    condition = models.ForeignKey(Conditions, on_delete=models.CASCADE, default=None, related_name="hotel_booking_condition")
    no_of_rooms = models.ForeignKey(Rooms, on_delete=models.CASCADE, default=None, related_name="hotel_booking_room")
    
    price = models.DecimalField(decimal_places=2, max_digits=20, default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.city} > {self.hotel.name} : {self.no_of_rooms.number} - {self.condition.name} > {self.price}"
        





class Gender(models.Model):
    type = models.CharField()

    def __str__(self):
        return f"{self.type}"
    

class Nations(models.Model):
    name = models.CharField()

    def __str__(self):
        return f"{self.name}"    
    

class Checkout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, default=None)
    
    # primary info
    first_name = models.CharField(max_length=250, default=None)
    last_name = models.CharField(max_length=250, default=None)
    middle_name = models.CharField(max_length=250, default=None)
    nationality = models.ForeignKey(Nations, on_delete=models.CASCADE, default=None, related_name="checkout_nationality")
    date_of_birth = models.DateField(default=None)
    gender= models.ForeignKey(Gender, on_delete=models.CASCADE, default=None)

    # traveling credentials
    passport_no = models.CharField(default=None)
    passport_expiry_date = models.DateField(default=None)
    passport_issuing_authority = models.ForeignKey(Nations, on_delete=models.CASCADE, default=None, related_name="checkout_passport_issuing_authority")
    # where to send confirmation
    contact = models.CharField(max_length=15)
    mail = models.EmailField()
    address = models.TextField()

    # others 
    seat_no = models.PositiveIntegerField(unique=False, null=True, blank=True)
    extra_luggage_quantity = models.CharField(default=0)
    extra_luggage_price = models.DecimalField(decimal_places=2, max_digits=20, default=0)

    total_fare = models.DecimalField(decimal_places=2, max_digits=20)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name}-{self.last_name}: {self.booking.depart_from} > {self.booking.destination}"
    



class HotelCheckout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    hotel_booking = models.ForeignKey(HotelBooking, on_delete=models.CASCADE, default=None)

    check_in = models.DateField(default=None, null=True, blank=True)
    check_out = models.DateField(default=None, null=True, blank=True)
    
    # primary info
    first_name = models.CharField(max_length=250, default=None)
    last_name = models.CharField(max_length=250, default=None)
    middle_name = models.CharField(max_length=250, default=None)
    nationality = models.ForeignKey(Nations, on_delete=models.CASCADE, default=None, related_name="hotel_checkout_nationality")
    date_of_birth = models.DateField(default=None)
    gender= models.ForeignKey(Gender, on_delete=models.CASCADE, default=None)

    # where to send confirmation
    contact = models.CharField(max_length=15)
    mail = models.EmailField()

    total_amount = models.DecimalField(decimal_places=2, max_digits=20)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name}-{self.last_name}: {self.hotel_booking.hotel.name} - {self.hotel_booking.check_in}"
    





class Flight_Status(models.Model):
    status = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.status}"
    

class Ticket(models.Model):
    checkout = models.ForeignKey(Checkout, on_delete=models.CASCADE)
    flight_status = models.ForeignKey(Flight_Status, on_delete=models.CASCADE, default=None)
    
    def __str__(self):
        return f"{self.checkout.first_name}: {self.flight_status}"
    





class Payment(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paystack_ref = models.CharField(max_length=15, blank=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'Payment {self.id}'

    def get_amount(self):
        return self.amount
