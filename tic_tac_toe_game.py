print('This is the Tic-tac-toe game!')
print('\n')
print("| X | O | O |")
print("|-X-|-X-|-X-|")
print("|   | 0 |   |")
print('\n')

input('Press Enter to start the game')

turns_counter = 1


def setup():
    # global empty_spots
    # empty_spots = input('Please choose the empty spots of the board: ') #if add  you can choose the empty spots
    global player_1_name, player_2_name
    global board
    # global turns_counter
    board = [[" ", " ", " "] for _ in range(3)]
    player_1_name = input('Enter player 1 name: ')
    player_2_name = input('Enter player 2 name: ')
    player_1_sign = input(f'{player_1_name}, please select a sign X or O: ')
    while player_1_sign.lower() not in ('x', 'o'):
        player_1_sign = input('Player 1, please select a sign X or O: ')
    player_1_sign = player_1_sign.upper()
    player_2_sign = 'O' if player_1_sign == 'X' else 'X'
    global player_signs, player_names
    player_signs = {1: player_1_sign, 0: player_2_sign}
    player_names = {1: player_1_name, 0: player_2_name}
    print('\n')
    print('This is the numeration of the board:')
    print("| 1 | 2 | 3 |")
    print("| 4 | 5 | 6 |")
    print("| 7 | 8 | 9 |")
    print('\n')
    print(f'{player_1_name} starts first')


def new_game(y_or_n):
    y_or_n = y_or_n.lower()
    if y_or_n == 'n':
        print(input('End of game. Pres enter to exit program'))
        exit()
    if y_or_n.lower != 'n' and y_or_n != 'y':
        print(f"Invalid input")
        print(f"Do you want new game? y/n")
        new_game(input())


    elif new_game == 'y':
        return
    setup()
    play()
    return new_game(input(f'Do you want a new game? y/n\n'))


positions_mapper = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2),
}


def draw_board(board):  # 5
    print('\n')
    print(f'Indices of the dashboard')
    print("| 1 | 2 | 3 |")
    print("| 4 | 5 | 6 |")
    print("| 7 | 8 | 9 |")

    print('\n')
    print('Current dashboard:')
    for row in range(len(board)):
        print(f"| {' | '.join(board[row])} |")
    print('\n')


def position_available(board, selected_pos, sign):  # 4
    raw = positions_mapper[selected_pos][0]
    column = positions_mapper[selected_pos][1]
    current_element = board[raw][column]
    if not current_element == ' ':
        return True
    return False


def play_turn(board, sign, selected_pos, turns_counter):  # 3  start from turn 2
    raw = positions_mapper[selected_pos][0]
    column = positions_mapper[selected_pos][1]
    current_element = board[raw][column]
    board[raw][column] = sign
    draw_board(board)


def is_position_is_valid(pos):  # 2
    if pos in range(1, 10):
        return True
    return False


def is_row_winner():  #
    for row_number in range(len(board)):
        if board[row_number][0] == board[row_number][1] == board[row_number][2] == ('X'):
            return  True
        elif board[row_number][0] == board[row_number][1] == board[row_number][2] == ('O'):
            return True
        return False


def is_col_winner():
    for col_number in range(len(board)):
        if board[0][col_number] == board[1][col_number] == board[2][col_number] != ' ':
            return True
    return False


def is_diagonal_winner():
    left_diagonal = board[0][0] == board[1][1] == board[2][2] != ' '
    right_diagonal = board[0][2] == board[1][1] == board[2][0] != ' '
    if left_diagonal or right_diagonal:
        return True
    return False


def has_won():  # 6
    if is_row_winner() or is_col_winner() or is_diagonal_winner():
        return True

    return False


def has_moves_more_9(counter):
    if counter >= 10:
        print(F'End of moves!')
        print(F'No one wins!')
        print('print(''Do you want new game? y/n')
        new_game(input())

        return True

    return False


def play():  # 1
    turns_counter = 1
    while not has_won():
        has_moves_more_9(turns_counter)
        current_selected_position = input(f"{player_names[turns_counter % 2]}, select an available position [1-9]: ")
        while not current_selected_position.isdigit():
            print('Invalid input')
            current_selected_position = input(f"{player_names[turns_counter % 2]}, select a position [1-9]: ")
        current_selected_position = int(current_selected_position)
        while not is_position_is_valid(current_selected_position):
            print('Invalid input')
            current_selected_position = input(f"{player_names[turns_counter % 2]}, select a position [1-9]: ")
            current_selected_position = int(current_selected_position)

        while position_available(board, current_selected_position, player_signs[turns_counter % 2]):
            print('Position is already filled in')
            current_selected_position = input(f"Select an available position [1-9]: ")
            current_selected_position = int(current_selected_position)
        play_turn(board, player_signs[turns_counter % 2], current_selected_position, turns_counter)
        turns_counter += 1
    print(f"End of game. Winner is {player_names[(turns_counter - 1) % 2]}!")


if __name__ == '__main__':
    setup()
    play()
    print('Do you want new game? y/n')

    new_game(input())
    print('pres enter to close program')
