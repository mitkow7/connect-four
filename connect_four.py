ROWS = 6
COLUMNS = 7

DIRECTIONS = {
    "up": (-1, 0),  # Directions
    "left": (0, -1),
    "up_left": (-1, -1),
    "up_right": (-1, 1),
}


class FullColumnError(Exception):
    pass


def travel_direction(board, row_index, col_index, row_move, col_move, player, sign):
    count = 0

    for i in range(1, 4):
        next_element_row_index = eval(f"{row_index} {sign} {row_move * i}")
        next_element_col_index = eval(f"{col_index} {sign} {col_move * i}")

        if not is_valid_place(next_element_row_index, next_element_col_index):
            break

        if board[next_element_row_index][next_element_col_index] != player:
            break

        count += 1

    return count


def is_valid_column(column):
    return 1 <= column <= COLUMNS


def is_valid_place(row_index, col_index):
    return 0 <= row_index < ROWS and 0 <= col_index < COLUMNS


def play_turn(board, column_index, player):
    for row_index in range(len(board) - 1, -1, -1):
        if board[row_index][column_index] == "⚪️":
            board[row_index][column_index] = player

            return row_index, column_index

    raise FullColumnError


def is_winner(board, row_index, col_index, player):
    for direction, values in DIRECTIONS.items():
        result = 1

        row_move, col_move = values

        direction_count = travel_direction(board, row_index, col_index, row_move, col_move, player, "+")
        opposite_direction_count = travel_direction(board, row_index, col_index, row_move, col_move, player, "-")

        result += direction_count + opposite_direction_count

        if result >= 4:
            return True

    return False


def display_board(play_board):
    print()
    for row in play_board:
        print(*row)


def main():
    board = [["⚪️" for _ in range(COLUMNS)] for _ in range(ROWS)]

    display_board(board)

    turn = 1
    while True:
        current_player = "🔴" if turn % 2 == 0 else "🟡"

        try:
            current_column = int(input(f"Player {current_player} turn, please enter a column: "))
        except ValueError:
            print("\n❌Invalid column!❌\nPlease try again!\n")
            continue

        if not is_valid_column(current_column):
            print(f"\n❌Invalid column!❌\nPlease enter column between 1 and {COLUMNS}!\n")
            continue

        column_index = current_column - 1

        try:
            row, col = play_turn(board, column_index, current_player)
            display_board(board)
        except FullColumnError:
            print("\nThis column is full, please select another one with available space!\n")
            continue

        turn += 1

        if is_winner(board, row, col, current_player):
            print(f"Player {current_player} wins!\n")
            break


if __name__ == "__main__":
    main()
