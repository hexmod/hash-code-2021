
# Represents and intersection
class Intersection:

    def __init__(self, id):
        self.id = id
        self.incoming_streets = []


    def add_incoming_street(self, street):
        self.incoming_streets.append(street)

    def num_incoming_streets(self):
        return len(self.incoming_streets)

    def ever_used(self):
        for street in self.incoming_streets:
            if street.usage != 0:
                return True
        return False
