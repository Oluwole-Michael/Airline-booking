from django.contrib import admin
from . models import *

# Register your models here.

admin.site.register(Flight_Letter)

admin.site.register(Airline)
admin.site.register(Trip_Round)
admin.site.register(Flight_Class)
admin.site.register(Offer)
admin.site.register(Location)
admin.site.register(Booking)

admin.site.register(Hotel)
admin.site.register(City)
admin.site.register(Conditions)
admin.site.register(Rooms)
admin.site.register(CheckInOut)
admin.site.register(HotelBooking)

admin.site.register(Nations)
admin.site.register(Gender)
admin.site.register(Checkout)
admin.site.register(HotelCheckout)

admin.site.register(Flight_Status)
admin.site.register(Ticket)

admin.site.register(Payment)