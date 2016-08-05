from os import system
from functools import reduce


def get_input(board, ship_tuple, taken):
    x_str = ''
    y_str = ''
    direction = ''
    (ship, spaces, abbrev) = ship_tuple

    print('Please place your ' + ship + ' (' + str(spaces) + ') in the format "x y direction".')

    try:
        [x_str, y_str, direction] = input().lower().split()
    except ValueError:
        print('Invalid input. Try again.')
        get_input(board, ship_tuple, taken)

    x = eval(x_str)
    y = eval(y_str)
    d = direction[0]

    if not (0 < y <= 10 and 0 < x <= 10):
        print('Invalid input. Try again.')
        get_input(board, ship_tuple, taken)

    y_prime = 21 - (y*2)
    if d == 'u':
        if not reduce(lambda a, b: a or b, [(x, i) in taken for i in range(y, y + spaces)], False):
            for i in range(0, spaces*2, 2):
                board[y_prime - i] = board[y_prime - i][:((x - 1) * 5)] \
                                     + '| ' + abbrev + ' ' \
                                     + board[y_prime - i][(x * 5):]
                taken.add((x, y + (i // 2)))
        else:
            print('Invalid input. Try again.')
            get_input(board, ship_tuple, taken)
    elif d == 'd':
        if not reduce(lambda a, b: a or b, [(x, i) in taken for i in range(y - spaces, y)], False):
            for i in range(0, spaces*2, 2):
                board[y_prime + i] = board[y_prime - i][:((x - 1) * 5)] \
                                     + '| ' + abbrev + ' ' + \
                                     board[y_prime - i][(x * 5):]
                taken.add((x, y - (i // 2)))
        else:
            print('Invalid input. Try again.')
            get_input(board, ship_tuple, taken)
    elif d == 'l':
        if not reduce(lambda a, b: a or b, [(i, y) in taken for i in range(x - spaces, x)], False):
            board[y_prime] = board[y_prime][:(x - spaces) * 5] \
                             + (('| ' + abbrev + ' ') * spaces) \
                             + board[y_prime][(x * 5):]
            for i in range(x - spaces + 1, x + 1):
                taken.add((i, y))
        else:
            print('Invalid input. Try again.')
            get_input(board, ship_tuple, taken)
    elif d == 'r':
        if not reduce(lambda a, b: a or b, [(i, y) in taken for i in range(x, x + spaces)], False):
            board[y_prime] = board[y_prime][:(x - 1) * 5] \
                             + (('| ' + abbrev + ' ') * spaces) \
                             + board[y_prime][5 * (x + spaces - 1):]
            for i in range(x, x + spaces):
                taken.add((i, y))
        else:
            print('Invalid input. Try again.')
            get_input(board, ship_tuple, taken)
    else:
        print('Invalid input. Try again.')
        get_input(board, ship_tuple, taken)

    # clears
    system('cls')

    for line in board:
        print(line)

    return board, taken
