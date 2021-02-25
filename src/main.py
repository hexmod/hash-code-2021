###############################
##
## HASH CODE ENTRY
##
## Usage: python main.py <path_to_source_file> <output_location>
##
###############################
import sys
from .utils.car import Car
from .utils.street import Street
from .utils.intersection import Intersection

def main(file_location, output_location):
    print("Running Hash Code Entry")
    # Hash Code here :)

    input_file = open(file_location, "r")

    line_num = 0
    duration = 0
    num_intersections = 0
    num_streets = 0
    num_cars = 0
    bonus = 0
    intersections = []
    streets = []
    cars = []
    for line in input_file:
        if line_num == 0:
            numbers = line.split(" ")
            duration = int(numbers[0])
            num_intersections = int(numbers[1])
            num_streets = int(numbers[2])
            num_cars = int(numbers[3])
            bonus = int(numbers[4])
            intersections = create_intersections(num_intersections)
        elif line_num <= num_streets:
            street_info = line.split(" ")
            a_street = Street(street_info[2], int(street_info[3]))
            streets.append(a_street)
            intersections[int(street_info[1])].add_incoming_street(a_street)
        else:
            car_info = line.split(" ")
            cars.append(Car(int(car_info[0]), car_info[1:]))
        line_num += 1
    input_file.close()
    print(f"Created {len(intersections)} intersections")
    print(f"Created {len(streets)} streets")
    print(f"Created {len(cars)} cars")


    # Output
    output_file = open(output_location, "w")
    output_file.write(f"{str(len(intersections))}\n")
    for inter in intersections:
        output_file.write(f"{str(inter.id)}\n")
        output_file.write(f"{str(inter.num_incoming_streets())}\n")
        for street in inter.incoming_streets:
            output_file.write(f"{street.name} 2\n")

    output_file.close()



def create_intersections(num):
    intersections = []
    for i in range(num):
        intersections.append(Intersection(i))
    return intersections


# When run from the terminal
if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])