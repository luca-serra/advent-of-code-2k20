# Part 1

def initialization(input_list):
    """Return the set of initial active cubes given the input list"""
    z = 0
    active_cubes = []
    for y in range(len(input_list)):
        for x in range(len(input_list)):
            if input_list[y][x] == "#":
                active_cubes.append((x, y, z))

    return set(active_cubes)


def get_coordinates_to_observe(active_set):
    """Return a set of coordinates of all potential active sites given the set of active cubes"""
    coordinates = []
    for coordinate in active_set:
        for x in [coordinate[0] - 1, coordinate[0], coordinate[0] + 1]:
            for y in [coordinate[1] - 1, coordinate[1], coordinate[1] + 1]:
                for z in [coordinate[2] - 1, coordinate[2], coordinate[2] + 1]:
                    if not ((x, y, z) in coordinates):
                        coordinates.append((x, y, z))

    return set(coordinates)


def becomes_active(coordinate, active_set):
    """Return True if the cube becomes active else False"""
    count_active = 0
    for x in [coordinate[0] - 1, coordinate[0], coordinate[0] + 1]:
        for y in [coordinate[1] - 1, coordinate[1], coordinate[1] + 1]:
            for z in [coordinate[2] - 1, coordinate[2], coordinate[2] + 1]:
                if (x, y, z) != coordinate and (x, y, z) in active_set:
                    count_active += 1
    if coordinate in active_set:
        if count_active in [2, 3]:
            return True
        return False
    else:
        if count_active == 3:
            return True
        return False


# Part 2

def initialization_2(input_list):
    """Return the set of initial active cubes given the input list"""
    z = 0
    w = 0
    active_cubes = []
    for y in range(len(input_list)):
        for x in range(len(input_list)):
            if input_list[y][x] == "#":
                active_cubes.append((x, y, z, w))

    return set(active_cubes)


def get_coordinates_to_observe_2(active_set):
    """Return a set of coordinates of all potential active sites given the set of active cubes"""
    coordinates = []
    for coordinate in active_set:
        for x in [coordinate[0] - 1, coordinate[0], coordinate[0] + 1]:
            for y in [coordinate[1] - 1, coordinate[1], coordinate[1] + 1]:
                for z in [coordinate[2] - 1, coordinate[2], coordinate[2] + 1]:
                    for w in [coordinate[3] - 1, coordinate[3], coordinate[3] + 1]:
                        if not ((x, y, z, w) in coordinates):
                            coordinates.append((x, y, z, w))

    return set(coordinates)


def becomes_active_2(coordinate, active_set):
    """Return True if the cube becomes active else False"""
    count_active = 0
    for x in [coordinate[0] - 1, coordinate[0], coordinate[0] + 1]:
        for y in [coordinate[1] - 1, coordinate[1], coordinate[1] + 1]:
            for z in [coordinate[2] - 1, coordinate[2], coordinate[2] + 1]:
                for w in [coordinate[3] - 1, coordinate[3], coordinate[3] + 1]:
                    if (x, y, z, w) != coordinate and (x, y, z, w) in active_set:
                        count_active += 1
    if coordinate in active_set:
        if count_active in [2, 3]:
            return True
        return False
    else:
        if count_active == 3:
            return True
        return False
