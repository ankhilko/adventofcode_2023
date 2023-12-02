from pprint import pprint


def adventofcode_2():

    allowed = {'red': 12, 'green': 13, 'blue': 14}

    with open('inputtext.txt') as file:
        new_data = file.read()
    data = new_data.split('\n')

    dataset_dict = {}

    ok_games = []

    for line in data:
        new_line = line.split(': ')
        key = int(new_line[0].strip().split(' ')[-1])

        dataset_dict[key] = {'red': 0, 'green': 0, 'blue': 0}

        values_sets = new_line[1].strip().split('; ')

        for value in values_sets:
            game_set = value.strip().split(', ')

            for cube in game_set:
                if dataset_dict[key][cube.split(' ')[-1]] < int(cube.split(' ')[0]):
                    dataset_dict[key][cube.split(' ')[-1]] = int(cube.split(' ')[0])

        for game in dataset_dict:

            for ball in dataset_dict[game]:
                if dataset_dict[game][ball] > allowed[ball]:
                    break
            else:
                ok_games.append(game)

    part1 = sum(set(ok_games))

    power = 0

    for game in dataset_dict:
        game_pow = 1
        for cube in dataset_dict[game]:
            game_pow *= dataset_dict[game][cube]

        power += game_pow

    part2 = power

    return part1, part2


if __name__ == '__main__':
    pprint(adventofcode_2())



