"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    return list(args)

def fix_list_of_wagons(each_wagons_id, missing_wagons):
    # 1. Seperate the first two misplaced wagon
    first_misplaced,second_misplaced, locomotive, *rest_of_wagons = each_wagons_id 
    # 2. Build the new train the correct order 
    return [locomotive, *missing_wagons, *rest_of_wagons, first_misplaced, second_misplaced]

def add_missing_stops(route, **stops):
    return {**route, "stops": list(stops.values())}
    
def extend_route_information(route, more_route_information):
    return {**route, **more_route_information}

def fix_wagon_depot(wagons_rows):
    return [list(row) for row in zip(*wagons_rows)]