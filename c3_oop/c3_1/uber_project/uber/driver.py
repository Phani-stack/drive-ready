# class
class Driver:

    total_drivers = 0

    # constructor
    def __init__(self, name = "", rating = 0.0, driver_id = 0, is_online = False):
        # member variables/instance variables
        self.name = name
        self.rating = rating
        self.driver_id = driver_id
        self.is_online = is_online
        Driver.increment_driver()

    # methods/member methods
    def accept_ride(self, ride_id):
        print(f"Ride accepted {ride_id} by {self.name}")
    def details(self):
        return self.name, self.rating, self.driver_id, self.is_online

    def increment_driver():
        Driver.total_drivers += 1

