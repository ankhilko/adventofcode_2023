
SEED_MAP_CASH = {}


def turn_to_dict(data: list, seed_no=None):

    global SEED_MAP_CASH

    SEED_MAP_CASH = {}

    seed_map = {data[0]: {}}
    print('proceeding', data[0])
    print('input_seeds:', seed_no)

    for seed in seed_no:
        for num, line in enumerate(data[1:]):
            seed_check = line.split(' ')
            if int(seed_check[1]) <= seed <= int(seed_check[1]) + int(seed_check[2]):
                print(f'{int(seed_check[1])} <= {seed} <= {int(seed_check[1]) + int(seed_check[2])}')

                # seed_range = list(range(int(seed_check[1]), int(seed_check[1]) + int(seed_check[2]) + 1))
                # soil_range = list(range(int(seed_check[0]), int(seed_check[0]) + int(seed_check[2]) + 1))
                #
                # seed_list = [int(i) for i in seed_range]
                # soil_list = [int(j) for j in soil_range]

                SEED_MAP_CASH[data[0]][seed] = int(seed_check[0]) - int(seed_check[1]) + seed
                # seed_map[data[0]].update(dict(zip(seed_list, soil_list)))

        # print(f'seed_map for line "{line}":', seed_map)

    ret_dict = {}

    print('FINAL seed_map: ', SEED_MAP_CASH)

    for seed in seed_no:
        if seed in SEED_MAP_CASH[data[0]]:
            ret_dict[seed] = SEED_MAP_CASH[data[0]][seed]
        else:
            ret_dict[seed] = seed

    soil_list = [ret_dict[i] for i in ret_dict]

    print('ret_dict:', ret_dict)
    print('soil_list:', soil_list)

    return soil_list


def extract_seed(data):
    to_int = data.strip().split(':')[1].strip().split(' ')
    as_list_of_tuples = []
    for k in range(len(to_int), 2):
        as_list_of_tuples.append((int(to_int[k]), int(to_int[k + 1])))

    return as_list_of_tuples


def adventofcode_5_1():
    '''
    31599214 5-1


    '''

    with open('inputtext_test.txt') as file:
        data = file.read()
    data_start = data.strip().strip('\n').split('\n\n')
    seed_no = extract_seed(data_start[0])
    seed_no.sort()

    seed_no_to_work = extract_seed(data_start[0])

    for k in range(0, len(seed_no), 2):
        seed_no_to_work += (seed_no[k], seed_no[k + 1])

    for line_1 in data_start[1:]:
        if not line_1.strip('\n') == '':
            new_line = line_1.strip('\n').split('\n')
            seed_no_to_work = turn_to_dict(new_line, seed_no=seed_no_to_work)

    return min(seed_no_to_work)


if __name__ == '__main__':
    print(adventofcode_5_1())

