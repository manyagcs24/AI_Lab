board = ["-"] * 9

def display_board():
    print()
    for i in range(0, 9, 3):
        print(board[i], board[i + 1], board[i + 2])
    print()


def check_win(player):
    winning_positions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for position in winning_positions:
        if all(board[i] == player for i in position):
            return True

    return False


def check_draw():
    return "-" not in board


while True:

    # Player 1
    print("P1 enter position")
    pos = int(input()) - 1

    if pos < 0 or pos > 8 or board[pos] != "-":
        print("Invalid position filled, reenter")
        continue

    board[pos] = "X"
    display_board()

    if check_win("X"):
        print("Player 1 wins!")
        break

    if check_draw():
        print("Draw!")
        break

    # Player 2
    print("P2 enter position")
    pos = int(input()) - 1

    if pos < 0 or pos > 8 or board[pos] != "-":
        print("Invalid position filled, reenter")
        continue

    board[pos] = "O"
    display_board()

    if check_win("O"):
        print("Player 2 wins!")
        break

    if check_draw():
        print("Draw!")
        break
