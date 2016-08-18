from model import *
from rentner import *


class Car(BaseModell):
    rentner = ForeignKeyField(Rentner, related_name='car', null=True)
    license_plate_number = CharField(unique=True)
    brand = CharField()
    brand_type = CharField()
    color = CharField()
    available = BooleanField()

    @property
    def auto_data(self):
        return self.license_plate_number+' '+self.brand+' '+self.brand_type+' '+self.color

    @classmethod
    def find_available_car(cls):
        query = cls.select().where(cls.available >> True)
        for i, car in enumerate(query):
            print(i+1, " ", car.auto_data)

    @classmethod
    def find_not_available_car(cls):
        query = cls.select().where(cls.available >> False)
        for i, car in enumerate(query):
            print(i+1, " ", car.auto_data)

    @classmethod
    def get_new_car(cls, l_p_number, brand, type_, color):
        new_car = Car.create(license_plate_number=l_p_number, brand=barnd,
                             brand_type=type_, color=color, available=True)
