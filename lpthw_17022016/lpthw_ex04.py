# -*- coding: utf-8 -*- Задава кодова таблица за  кирлицата https://www.python.org/dev/peps/pep-0263/

cars = 100 #number of cars
space_in_a_car = 4.0 #available space for passengers
drivers = 30 #available drivers
passengers = 90
cars_driven = drivers #available drivers
cars_not_driven = cars - drivers #
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "Ther are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empy cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "passengers to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."