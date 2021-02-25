
# Represents a street
class Street:

    def __init__(self, name, length):
        self.name = name
        self.length = length
        self.usage = 0

    def add_usage(self):
        self.usage += 1
