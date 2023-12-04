def find_l(i, j, data):
    pass


def find_r(i, j, data):
    pass


def find_o(i, j, data):
    pass


def adventofcode_4_1():
    '''
    o
    '''

    with open('inputtext.txt') as file:
        data = file.read()
    data = data.strip().split('\n')
    mult = 0

    for i, line in enumerate(data):
        if '*' in line:
            if i == 0:
                pass
            if i == len(line) - 1:
                pass
            new_gear = []
            for j, char in enumerate(line):
                if data[i][j] == '*':
                    new_gear = []
                    if data[i][j - 1] in '0123456789':
                        try:
                            new_gear += find_l(i, j, data)
                        except TypeError:
                            pass
                    if data[i][j + 1] in '0123456789':
                        try:
                            new_gear += find_r(i, j, data)
                        except TypeError:
                            pass
                    if i > 0:
                        try:
                            new_gear += find_o(i - 1, j, data)
                        except TypeError:
                            pass

                    if i < len(data) - 1:
                        try:
                            new_gear += find_o(i + 1, j, data)
                        except TypeError:
                            pass
                if len(new_gear) == 2:
                    mult += new_gear[0] * new_gear[1]
                new_gear = []

    return mult


if __name__ == '__main__':
    print(adventofcode_4_1())

