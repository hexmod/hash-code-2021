
# Represents a street
class Street:

    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.usage = 0
        self.starting_cars = 0

    def add_usage(self):
        self.usage += 1

    def set_usage(self, usage):
        self.usage = usage

    def add_starting_cars(self):
        self.starting_cars += 1

    def set_starting_cars(self, value):
        self.starting_cars = value