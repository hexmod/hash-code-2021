###############################
##
## HASH CODE ENTRY
##
## Usage: python main.py <path_to_source_file> <output_location>
##
###############################
import sys
import os
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

    # Check street usage
    add_street_usage(cars, streets, file_location)

    # Check inter usage
    used_intersections = list(filter(lambda x: x.ever_used(), intersections))
    
    # Output
    output_file = open(output_location, "w")
    output_file.write(f"{str(len(used_intersections))}\n")
    for inter in used_intersections:
        output_file.write(f"{str(inter.id)}\n")
        used_streets = list(filter(lambda x: x.usage > 0, inter.incoming_streets))
        output_file.write(f"{str(len(used_streets))}\n")

        used_streets.sort(key=lambda x: x.starting_cars, reverse=True)
        for street in used_streets:
            output_file.write(f"{street.name} 1\n")

    output_file.close()



def create_intersections(num):
    intersections = []
    for i in range(num):
        intersections.append(Intersection(i))
    return intersections


def add_street_usage(cars, streets, file_location):
    head_tail = os.path.split(file_location) 
    file_name = os.path.join(".\cache", head_tail[1])

    if os.path.isfile(file_name):
        print("Using Cache")
        input_file = open(file_name, "r")
        count = 0
        for line in input_file:
            values = line.split(" ")
            streets[count].set_usage(int(values[0]))
            streets[count].set_starting_cars(int(values[1]))
            count += 1
    else:
        print("Writing Cache")
        for a_car in cars:
            first = True
            for street_name in a_car.roads:
                for a_street in streets:
                    if a_street.name == street_name:
                        a_street.add_usage()
                        if first:
                            a_street.add_starting_cars()
                        break
                first = False

        # Write street usage to file as cache
        output_file = open(file_name, "w")
        for s in streets:
            output_file.write(f"{s.usage} {s.starting_cars}\n")


# When run from the terminal
if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])