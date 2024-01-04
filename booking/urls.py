from django.urls import path
from . import views


urlpatterns = [
    path("", views.Home, name="home"),
    path("letter", views.FlightLetter, name="letter"),

    # flight
    path("booking-filter", views.BookingFilter, name="booking_filter"),
    path("sort/<str:sort_booking>/", views.SortBookingFilter, name="sort"),
    path("book/<str:id>/", views.Book, name="book"),
    path("checkout", views.BookingCheckout, name="checkout"),

    # hotel
    path("hotel-filter", views.HotelBookingFilter, name="hotel_filter"),
    path("hotel-book/<str:id>/", views.HotelBook, name="hotel_book"),
    path("hotel-checkout", views.HotelBookingCheckout, name="hotel_checkout"),

    path("register", views.Register, name="register"),
    path("login", views.Login, name="login"),
    path("logout", views.Logout, name="logout"),

    path('payment/', views.payment_init, name='create'),
    path('process/', views.payment_process, name='process'), 
    path('success/', views.payment_success, name='success'), 
    path('canceled/', views.payment_canceled, name='canceled'), 
]