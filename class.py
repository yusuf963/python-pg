
# ! classes

class Car:
    def __init__(self, color, seats):
        self.color = color
        self.seats = seats
        self.pssenger = []

    def addPassenger(self, passenger):
        self.pssenger.append(passenger)

    def __str__(self):
        return f"my car is a {self.color} car, with {self.seats} seats"


nicks_car = Car('red', 4)
print(nicks_car)


class Tesla(Car):
    def __init__(self, color, seats, battery_level):
        Car.__init__(self, color, seats)
        self.battery_level = battery_level
    def __str__(self):
        return f"my car is a {self.color} car, with {self.seats} seats"
     