def adventofcode_2():
    with open('task1input.txt') as file:
        new_data = file.read()
    data = new_data.split()
    digs = [str(i) for i in range(1, 10)] + ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    digs_dic = dict(zip(digs, list(range(1, 10)) + list(range(1, 10))))
    sum = 0

    for line in data:
        first_dig = None
        last_dig = None
        line_to = line[:]
        while len(line_to) > 0:
            for item in digs_dic:

                if line_to.startswith(item):
                    if not first_dig:
                        first_dig = digs_dic[item]
                    last_dig = digs_dic[item]
            line_to = line_to[1:]
        if first_dig:
            coordinates = int(str(first_dig) + str(last_dig))
            sum += coordinates

    print('sum = ', sum)
