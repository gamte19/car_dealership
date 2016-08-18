from model import *


class Rentner(BaseModell):
    first_name = CharField()
    last_name = CharField()
    driver_licence_number = CharField()

    @property
    def full_name(self):
        return self.first_name+" "+self.last_name
