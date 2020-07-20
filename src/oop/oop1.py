# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

class Vehicle:
    pass
    # def __init__(self, vehicle):
    #     self.vehicle = vehicle
class FlightVehicle(Vehicle):
    pass
    # def __init__(self, flight_vehicle):
    #     super().__init__(flight_vehicle)
class Starship(FlightVehicle):
    pass
    # def __init__(self, starship):
    #     super().__init__(starship)
class GroundVehicle(Vehicle):
    pass
    # def __init__(self, ground_vehicle):
    #     super().__init__(ground_vehicle)
class Airplane(FlightVehicle):
    pass
    # def __init__(self, airplane):
    #     super().__init__(airplane)
class Car(GroundVehicle):
    pass
    # def __init__(self, car):
    #     super().__init__(car)
class Motorcycle(GroundVehicle):
    pass
    # def __init__(self, motorcycle):
    #     super().__init__(motorcycle)
