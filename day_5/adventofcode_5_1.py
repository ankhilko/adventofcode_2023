
SEED_MAP_CASH_TEMP = []
TEMP = []


def turn_to_dict(data: list, seed_no=None):
    pass


def start_with_extract_seeds(data):
    global SEED_MAP_CASH_TEMP, TEMP

    """
    turn plain list of starting seeds to 2 num tuple list
    """
    to_int = data.strip().split(':')[1].strip().split(' ')
    as_list_of_tuples = []
    for k in range(0, len(to_int), 2):
        as_list_of_tuples.append((int(to_int[k]), int(to_int[k + 1])))

    return as_list_of_tuples


def seed_soil_array_check(a: list, b: list, soil: int):
    global SEED_MAP_CASH_TEMP, TEMP

    rest_of_a = []

    resulting_b = []

    print(a, b, soil)

    if a[0] >= b[0]:
        if a[0] + a[1] <= b[0] + b[1]:
            """
            first check
            """
            print('first = OK')

            resulting_b = [soil + (a[0] - b[0]), a[1]]

        elif b[0] <= a[0] + a[1] <= b[0] + b[1]:
            """
            second check
            """
            print('second = OK')

            resulting_b = [soil + (a[0] - b[0]), ]
            rest_of_a.append([a[0] + (b[1] - (a[0] - b[0])), a[1] - (b[1] - (a[0] - b[0]))])
        else:
            rest_of_a = a
    elif a[0] <= b[0]:
        if a[0] + a[1] >= b[0] + b[1]:
            """
            third check
            """
            print('third = OK')

            resulting_b = [soil, b[1]]
            rest_of_a.append([a[0], a[0] - b[0]])
            rest_of_a.append([a[0] + (a[0] - b[0]) + b[1], a[1] - (a[0] - b[0]) - b[1]])
        elif b[0] <= a[0] + a[1] <= b[0] + b[1]:
            """
            fourth check
            """
            print('fourth = OK')

            resulting_b = [soil, a[1] - (a[0] - b[0])]
            rest_of_a.append([a[0], a[0] - b[0]])
        else:
            rest_of_a = a

    if not resulting_b:
        print('No soil found')
    if not resulting_b and not rest_of_a:
        print('all seed to check again')
        print('the rest of seeds', rest_of_a)
    if rest_of_a:
        print('the rest of seeds', rest_of_a)

    return [resulting_b, rest_of_a]


def soil_array_to_nos(text: str):
    global SEED_MAP_CASH_TEMP, TEMP

    soil, seed, length = int(text[0]), int(text[1]), int(text[2])
    return [seed, length], soil


def seed_nos_to_soil_nos(set_of_seeds, data_s_s):
    global SEED_MAP_CASH_TEMP, TEMP

    # global SEED_MAP_CASH_TEMP
    # SEED_MAP_CASH_TEMP = set_of_seeds

    # for line in data_s_s:
    soil = int(data_s_s[0])
    b = [int(data_s_s[1]), int(data_s_s[2])]
    print()
    print()
    print('seeds=', set_of_seeds, 'b=', b, 'soil=', soil)
    result = seed_soil_array_check(set_of_seeds, b, soil)

    if result[0]:
        TEMP.append(result[0])

    return result


def do_one_part(data_in):
    global SEED_MAP_CASH_TEMP, TEMP

    data_in = data_in.split('\n')

    for seeds in SEED_MAP_CASH_TEMP:

        for data_s_s_set in data_in[1:]:

            print('data_in', data_in)
            print('data_s_s_set', data_s_s_set)

            data_s_s_set = data_s_s_set.split(' ')

            soils, seeds = seed_nos_to_soil_nos(seeds, data_s_s_set)

            print()

        print('rest of seeds', seeds)
        print('soils ', TEMP)



def adventofcode_5_2():
    """
    Reads input from a file, extracts a seed number, and returns the soil number.
    """
    # Open the file and read the content

    global SEED_MAP_CASH_TEMP, TEMP
    with open('inputtext_test.txt') as file:
        data = file.read()

    # Extract the soil number from the data
    data_start = data.strip().strip('\n').split('\n\n')

    print('data_start[1:] ', data_start[1:])

    seed_nos_to_work = start_with_extract_seeds(data_start[0])

    SEED_MAP_CASH_TEMP = seed_nos_to_work

    print('SEED_MAP_CASH_TEMP', SEED_MAP_CASH_TEMP)

    for soil_in in data_start[1:]:
        print('soil_in', soil_in)

        do_one_part(soil_in)

        print('data_start[soil_in]', soil_in)

        SEED_MAP_CASH_TEMP = TEMP
        TEMP = []

    return SEED_MAP_CASH_TEMP


if __name__ == '__main__':
    print(adventofcode_5_2())


