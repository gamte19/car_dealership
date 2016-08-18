from rentner import *
from car import *
from booking import *

Booking.delete().execute()
Car.delete().execute()
Rentner.delete().execute()

rentner_1 = Rentner.create(first_name='Pisti', last_name='Sanyi', driver_licence_number='HU1234')
rentner_2 = Rentner.create(first_name='Laci', last_name='Kiss', driver_licence_number='HU1544')
rentner_3 = Rentner.create(first_name='Geza', last_name='Pityu', driver_licence_number='HU1764')

car_1 = Car.create(rentner=rentner_1, license_plate_number='AAA-111',
                   brand='BMW', brand_type='5', color='black', available=False)
car_2 = Car.create(license_plate_number='BBB-222',
                   brand='Opel', brand_type='Corsa', color='white', available=False)
car_3 = Car.create(rentner=rentner_1, license_plate_number='CCC-333',
                   brand='Audi', brand_type='A5', color='black', available=False)
car_4 = Car.create(license_plate_number='DDD-444', brand='Toyota', brand_type='Corolla', color='pink', available=True)
car_5 = Car.create(rentner=rentner_3, license_plate_number='EEE-555',
                   brand='Honda', brand_type='Civic', color='yellow', available=False)

booked_1 = Booking.create(car=car_1, rentner=rentner_3, start_date='2016-05-22', end_date='2016-05-25')
booked_2 = Booking.create(car=car_2, rentner=rentner_3, start_date='2016-04-20', end_date='2016-04-12')
booked_3 = Booking.create(car=car_5, rentner=rentner_2, start_date='2016-05-18', end_date='2016-05-23')
booked_4 = Booking.create(car=car_3, rentner=rentner_1, start_date='2016-06-15', end_date='2016-06-09')
