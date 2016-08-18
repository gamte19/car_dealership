from car import *
from rentner import *


class Booking(BaseModell):
    car = ForeignKeyField(Car, related_name='slot')
    rentner = ForeignKeyField(Rentner, related_name='slot')
    start_date = DateField()
    end_date = DateField()

    @classmethod
    def rent_car(cls, car_number, f_name, l_name, d_l_number, start, end):
        query = Car.select().where(Car.available >> True)
        for i, car in enumerate(query):
            if i+1 == int(car_number):
                Car.update(available=False).where(Car.id == car.id).execute()
                new_rentner = Rentner.create(first_name=f_name, last_name=l_name, driver_licence_number=d_l_number)
                new_booking = Booking.create(car=car.id, rentner=new_rentner.id, start_date=start, end_date=end)

    @classmethod
    def car_back(cls):
        Car.find_not_available_car()
        license = 'CCC-333'
        try:
            query = (Booking.select().join(Car).where(Car.license_plate_number == license).get())
            Car.update(available=True).where(Car.license_plate_number == license).execute()
            Booking.delete().where(cls.id == query.id).execute()
        except:
            print("Not exists in the database")
Booking.car_back()
