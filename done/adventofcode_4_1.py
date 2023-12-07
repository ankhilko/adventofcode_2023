def adventofcode_4_1():
    '''
    o
    '''

    with open('inputtext.txt') as file:
        data = file.read()
    data = data.strip().split('\n')

    points_total = 0

    for card in data:
        edited_card = card.replace('  ', ' ')
        card_win_numbers, card_numbers = edited_card.split('|')
        card_win_numbers = card_win_numbers.strip().split(':')[1].strip().split(' ')
        card_numbers = card_numbers.strip().split(' ')
        card_numbers = [int(i) for i in card_numbers]
        card_win_numbers = [int(i) for i in card_win_numbers]

        hits = len([i for i in card_win_numbers if i in card_numbers])

        if hits > 0:
            points_total += 2**(hits - 1)

    return points_total


def adventofcode_4_2():
    '''
    o
    '''

    with open('inputtext.txt') as file:
        data = file.read()
    data = data.strip().split('\n')

    card_nums = len(data)
    card_deck = dict(zip(range(card_nums), (1 for _ in range(card_nums))))

    cards_total = 0
    points_total = 0

    for num, card in enumerate(data):
        step = 0

        print('for num, card in enumerate(data): ', num, ': ', card)
        print('step: ', step)

        while step < card_deck[num]:
            edited_card = card.replace('  ', ' ')
            card_win_numbers, card_numbers = edited_card.split('|')
            card_win_numbers = card_win_numbers.strip().split(':')[1].strip().split(' ')
            card_numbers = card_numbers.strip().split(' ')
            card_numbers = [int(i) for i in card_numbers]
            card_win_numbers = [int(i) for i in card_win_numbers]

            hits = len([i for i in card_win_numbers if i in card_numbers])

            if hits > 0:
                points_total += 2**(hits - 1)

            for j in range(1, min(hits + 1, card_nums - num + 1)):
                card_deck[num + j] += 1

            step += 1

    for key in card_deck:
        cards_total += card_deck[key]

    return points_total, cards_total


if __name__ == '__main__':
    print(adventofcode_4_2())

