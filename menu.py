from car import *
from booking import *


# print(Car.find_available_car())


def rent_car_menu():
    print("The following cars are available:")
    Car.find_available_car()
    car_number = input("Enter a number")
    f_name = input("first name")
    l_name = input("last name")
    d_l_number = input("driver license_plate_number")
    start = input("start")
    end = input("end")
    Booking.rent_car(car_number, f_name, l_name, d_l_number, start, end)


def car_backk():
    Car.find_not_available_car()
    license_plate_number = input("Enter the license plate number: ")
    Booking.car_back(license_plate_number)

#rent_car_menu()
car_backk()
