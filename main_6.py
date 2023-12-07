
def get_data_from_file(filename):
    with open(filename) as file:
        data = file.read()
    data = data.strip('\n')
    data = data.split('\n')

    print(data)

    time, distance = data[0].split(), data[1].split()

    print(time)
    print(distance)

    dict()


def main():
    get_data_from_file('test.txt')


if __name__ == '__main__':
    main()
