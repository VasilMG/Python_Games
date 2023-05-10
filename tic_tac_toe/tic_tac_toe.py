def read_players():
    player_one_name = input('Player one name:')
    player_two_name = input('Player two name:')

    player_one_sign = input(f"{player_one_name} would you like to play with 'X' or 'O'").upper()
    while player_one_sign not in ['X', 'O']:
        player_one_sign = input(f"{player_one_name} would you like to play with 'X' or 'O'").upper()

    player_two_sign = 'O' if player_one_sign == 'X' else "X"

    return [(player_one_name, player_one_sign), (player_two_name, player_two_sign)]

def print_board(board):
    for row in range(len(board)):
        print('|', end="")
        for column in range(len(board)):
            print(f"  {' ' if board[row][column] is None else board[row][column]}  |", end="")
        print()


def get_board(n):
    board = [[None] * n for _ in range(n)]
    return board

board = get_board(3)
print(board)

def print_board_numeration(board):
    print('This is the numeration of the board:')
    indx = 1
    for row in range(len(board)):
        print('|', end="")
        for column in range(len(board)):
            print(f"  {indx}  |", end="")
            indx += 1
        print()

def check_for_win(sign, player_row, player_column, board):
    won = True

    for col in range(len(board)):
        if board[player_row][col] != sign:
            won = False
            break

    if won:
        return True

    won = True
    for row in range(len(board)):
        if board[row][player_column] != sign:
            won = False
            break
    if won:
        return True

    won = True
    for indx in range(len(board)):
        if board[indx][indx] != sign:
            won = False
            break
    if won:
        return True

    won = True
    for indx in range(len(board)):
        if board[indx][len(board) -1 -indx] != sign:
            won = False
            break

    if won:
        return True

def is_draw(board):
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] is None:
                return False
    return True





def play_game(players, board, positions_mapping):
    print(f"{players[0][0]} starts first!")
    while True:
        player_name, player_sign = players[0]
        position_as_string = input(f"{player_name} please choose a free position [1-{len(board) * len(board)}]")
        if not position_as_string.isdigit():
            continue

        position = int(position_as_string)
        if position not in positions_mapping:
            continue

        row, column = positions_mapping[position]

        if board[row][column] is not None:
            continue
        board[row][column] = player_sign
        print_board(board)
        if check_for_win(player_sign, row, column, board):
            print(f"{player_name} wins!")
            break
        if is_draw(board):
            print('Draw!')
            break
        players[0], players[1] = players[1], players[0]



def get_positions_mapping(board):
    result = {}
    indx = 1
    for row in range(len(board)):
        for column in range(len(board)):
            result[indx] = (row, column)
            indx += 1
    return result


positions_mapping = get_positions_mapping(board)

play_game(read_players(),get_board(3),positions_mapping)
