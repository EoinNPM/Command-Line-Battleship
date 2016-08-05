from input import get_input

BLANK_BOARD = ['+ -- + -- + -- + -- + -- + -- + -- + -- + -- + -- +',
               '|    |    |    |    |    |    |    |    |    |    |',
               '+ -- + -- + -- + -- + -- + -- + -- + -- + -- + -- +',
               '|    |    |    |    |    |    |    |    |    |    |',
               '+ -- + -- + -- + -- + -- + -- + -- + -- + -- + -- +',
               '|    |    |    |    |    |    |    |    |    |    |',
               '+ -- + -- + -- + -- + -- + -- + -- + -- + -- + -- +',
               '|    |    |    |    |    |    |    |    |    |    |',
               '+ -- + -- + -- + -- + -- + -- + -- + -- + -- + -- +',
               '|    |    |    |    |    |    |    |    |    |    |',
               '+ -- + -- + -- + -- + -- + -- + -- + -- + -- + -- +',
               '|    |    |    |    |    |    |    |    |    |    |',
               '+ -- + -- + -- + -- + -- + -- + -- + -- + -- + -- +',
               '|    |    |    |    |    |    |    |    |    |    |',
               '+ -- + -- + -- + -- + -- + -- + -- + -- + -- + -- +',
               '|    |    |    |    |    |    |    |    |    |    |',
               '+ -- + -- + -- + -- + -- + -- + -- + -- + -- + -- +',
               '|    |    |    |    |    |    |    |    |    |    |',
               '+ -- + -- + -- + -- + -- + -- + -- + -- + -- + -- +',
               '|    |    |    |    |    |    |    |    |    |    |',
               '+ -- + -- + -- + -- + -- + -- + -- + -- + -- + -- +']

SHIP_LIST = [('Destroyer', 2, 'd2'),
             ('Cruiser', 3, 'c3'),
             ('Submarine', 3, 's3'),
             ('Battleship', 4, 'b4'),
             ('Aircraft Carrier', 5, 'a5')]


if __name__ == '__main__':
    board = BLANK_BOARD
    taken = set()

    for ship_tuple in SHIP_LIST:
        board, taken = get_input(board, ship_tuple, taken)
