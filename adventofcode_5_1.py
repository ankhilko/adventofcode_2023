
SEED_MAP_CASH_TEMP = []


def turn_to_dict(data: list, seed_no=None):
    pass


def start_with_extract_seeds(data):
    """
    turn plain list of starting seeds to 2 num tuple list
    """
    to_int = data.strip().split(':')[1].strip().split(' ')
    as_list_of_tuples = []
    for k in range(0, len(to_int), 2):
        as_list_of_tuples.append((int(to_int[k]), int(to_int[k + 1])))

    return as_list_of_tuples


def seed_soil_array_check(a: list, b: list, soil: int):

    rest_of_a = []

    resulting_b = []

    if a[0] >= b[0]:
        if a[0] + a[1] <= b[0] + b[1]:
            resulting_b = [soil + (b[0] - a[0]), a[1]]
        elif b[0] <= a[1] <= b[0] + b[1]:
            resulting_b = [soil + (b[0] - a[0]), ]
            rest_of_a.append([a[0] + (b[1] - (b[0] - a[0])), a[1] - (b[1] - (b[0] - a[0]))])
    elif a[0] <= b[0]:
        if a[0] + a[1] >= b[0] + b[1]:
            resulting_b = [soil, b[1]]
            rest_of_a.append([a[0], a[0] - b[0]])
            rest_of_a.append([a[0] + (a[0] - b[0]) + b[1], a[1] - (a[0] - b[0]) - b[1]])
        elif b[0] <= a[0] + a[1] <= b[0] + b[1]:
            resulting_b = [soil, a[1] - (a[0] - b[0])]
            rest_of_a.append([a[0], a[0] - b[0]])
    return [resulting_b, rest_of_a]


def adventofcode_5_2():
    """
    Reads input from a file, extracts a seed number, and returns the soil number.
    """
    # Open the file and read the content
    with open('inputtext_test.txt') as file:
        data = file.read()

    # Extract the soil number from the data
    data_start = data.strip().strip('\n').split('\n\n')
    soil_no_to_work = start_with_extract_seeds(data_start[0])

    return soil_no_to_work


if __name__ == '__main__':
    print(adventofcode_5_2())


