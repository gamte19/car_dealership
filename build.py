from booking import *
from rentner import *
from car import *

db.create_tables([Rentner, Car, Booking], safe=True)
