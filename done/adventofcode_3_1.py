
def find_l(i, j, data):
    temp = ''
    if data[i][j - 1] in '0123456789':
        for k in range(1, 4):
            if data[i][j - k] in '0123456789':
                temp = data[i][j - k] + temp
            else:
                break
    return [int(temp)]


def find_r(i, j, data):
    temp = ''
    if data[i][j + 1] in '0123456789':
        for k in range(1, 4):
            if data[i][j + k] in '0123456789':
                temp = temp + data[i][j + k]
            else:
                break
    return [int(temp)]


def find_o(i, j, data):
    templ = ''
    tempr = ''
    if data[i][j] in '0123456789':
        temp = data[i][j]
        if data[i][j - 1] in '0123456789' and data[i][j + 1] in '0123456789':
            temp = data[i][j - 1:j + 2]
        elif data[i][j - 1] in '0123456789':
            temp = data[i][j - 1] + temp
            if data[i][j - 2] in '0123456789':
                temp = data[i][j - 2] + temp
        elif data[i][j + 1] in '0123456789':
            temp += data[i][j + 1]
            if data[i][j + 2] in '0123456789':
                temp += data[i][j + 2]
        return [int(temp)]
    else:
        if data[i][j - 1] in '0123456789':
            templ = data[i][j - 1]
            if data[i][j - 2] in '0123456789':
                templ = data[i][j - 2] + templ
                if data[i][j - 3] in '0123456789':
                    templ = data[i][j - 3] + templ
        if data[i][j + 1] in '0123456789':
            tempr = data[i][j + 1]
            if data[i][j + 2] in '0123456789':
                tempr += data[i][j + 2]
                if data[i][j + 3] in '0123456789':
                    tempr += data[i][j + 3]
        if templ and not tempr:
            return [int(templ)]
        elif tempr and not templ:
            return [int(tempr)]
        elif templ and tempr:
            return [int(templ), int(tempr)]


def adventofcode_3():
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


def adventofcode_3_part_1():
    def check_num(i: int, j: int, temp: str, line, char=''):
        mass_1, mass_2, chars_2_check = '', '', ''
        if i > 0:
            mass_1 = data[i - 1][max(j - len(temp) - 1, 0):j + 1 if j < len(line) - 1 else j + 1]
        if i < len(data) - 1:
            mass_2 = data[i + 1][max(j - len(temp) - 1, 0):j + 1 if j < len(line) - 1 else j + 1]
        if not j - len(temp) == 0:
            chars_2_check = line[j - len(temp) - 1]
        all_mass = ''.join(list(mass_1) + list(mass_2) + [chars_2_check] + [char])
        all_mass = all_mass.replace('.', '')
        if all_mass:
            return int(temp)
        return 0

    with open('inputtext.txt') as file:
        data = file.read()
    data = data.strip().split('\n')
    sum = 0
    for i, line in enumerate(data):
        print('line', line)
        temp_num = ''
        all_mass = []
        for j, char in enumerate(line):
            if char in '0123456789':
                temp_num += char
                mass_1, mass_2, chars_2_check = [], [], []
                if j == len(line) - 1:
                    sum_old = sum
                    sum += check_num(i, j + 1, temp_num, line)
                    temp_num = ''
            else:
                if not temp_num == '':
                    sum_old = sum
                    sum += check_num(i, j, temp_num, line, char)
                    temp_num = ''
    return sum


if __name__ == '__main__':
    print(adventofcode_3())



