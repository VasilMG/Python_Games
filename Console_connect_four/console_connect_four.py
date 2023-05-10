def get_initial_field(rows_count, columns_count):
    return [[None] * columns_count for _ in range(rows_count)]
def print_field(field):
    [print([x if x else 0 for x in row]) for row in field]

def get_player_move(player): 
    player_move_str = input(f' Player {player} please choose a column.')
    player_move = int(player_move_str)
    return player_move - 1 

def apply_player_move_genn(max_row, column_count): 
    free_buttom_row_indeces = [max_row] * column_count 
    def apply_player_move(player, player_move, field): 
        player_row = free_buttom_row_indeces[player_move] 
        field[player_row][player_move] = player
        print(free_buttom_row_indeces)
        free_buttom_row_indeces[player_move] -= 1
    return apply_player_move 
                          
def is_win_condition(field):
    pass

def play(field):
    row_count = len(field)
    col_count = len(field[0])
    apply_player_move = apply_player_move_genn(row_count, col_count)
    current_player, other_player = 1, 2
    while True:
        player_move = get_player_move(current_player)
        apply_player_move(current_player, player_move, field)
        if in_win_condition(field):
            break
        else:
            current_player, other_player = other_player, current_player
            print_winner(field)

field = get_initial_field(5, 7)
play(field)