from abc import ABC, abstractmethod


class Car(ABC):
    def mileage(self):
        pass


class Tesla(Car):
    def mileage(self):
        print("The mileage is 40kmph")


class Suzuki(Car):
    def mileage(self):
        print("The mileage is 30kmph ")


class Duster(Car):
    def mileage(self):
        print("The mileage is 42kmph ")


class Renault(Car):
    def mileage(self):
        print("The mileage is 35kmph ")

    # Driver code


t = Tesla()
t.mileage()

r = Renault()
r.mileage()
s = Suzuki()
s.mileage()
d = Duster()
d.mileage()