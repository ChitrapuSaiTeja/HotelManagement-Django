from django.db import models
from django.contrib.auth.models import User

class Hotels(models.Model):
    #h_id,h_name,owner ,location,rooms
    name = models.CharField(max_length=30, default="Broomk")
    owner = models.CharField(max_length=20)
    location = models.CharField(max_length=50)
    state = models.CharField(max_length=50, default="Punjab")
    country = models.CharField(max_length=50, default="India")

    def __str__(self):
        return self.name

class Rooms(models.Model):
    ROOM_STATUS = (
        ("1", "available"),
        ("2", "not available"),
    )

    ROOM_TYPE = (
        ("1", "premium"),
        ("2", "deluxe"),
        ("3", "regular"),
    )

    room_type = models.CharField(max_length=50, choices=ROOM_TYPE)
    capacity = models.IntegerField()
    price = models.IntegerField(default=0)
    size = models.IntegerField()
    hotel = models.ForeignKey(Hotels, on_delete=models.CASCADE)
    status = models.CharField(choices=ROOM_STATUS, max_length=15)
    roomnumber = models.IntegerField()
    payprice = models.IntegerField(default=0)  # Add the payprice field

    def __str__(self):
        return f"{self.hotel.name}{self.roomnumber}"

class Reservation(models.Model):
    check_in = models.DateField(auto_now=False)
    check_out = models.DateField()
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    guest = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_id = models.CharField(max_length=100, default="null")

    def __str__(self):
        return self.guest.username
