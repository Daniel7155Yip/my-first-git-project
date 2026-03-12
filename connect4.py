ROWS = 6
COLS = 7

def make_board():
    return [[" "] * COLS for _ in range(ROWS)]

def print_board(board):
    for row in board:
        print("|" + "|".join(row) + "|")
    print("+" + "-+" * COLS)
    print(" " + " ".join(str(i + 1) for i in range(COLS)))

def drop_piece(board, col, player):
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == " ":
            board[row][col] = player
            return row
    return -1

def check_winner(board, player):
    # Horizontal
    for r in range(ROWS):
        for c in range(COLS - 3):
            if all(board[r][c + i] == player for i in range(4)):
                return True
    # Vertical
    for r in range(ROWS - 3):
        for c in range(COLS):
            if all(board[r + i][c] == player for i in range(4)):
                return True
    # Diagonal down-right
    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if all(board[r + i][c + i] == player for i in range(4)):
                return True
    # Diagonal down-left
    for r in range(ROWS - 3):
        for c in range(3, COLS):
            if all(board[r + i][c - i] == player for i in range(4)):
                return True
    return False

def is_full(board):
    return all(board[0][c] != " " for c in range(COLS))

def get_move(player):
    while True:
        try:
            col = int(input(f"Player {player}, choose a column (1-{COLS}): ")) - 1
            if 0 <= col < COLS:
                return col
            print(f"Please enter a number between 1 and {COLS}.")
        except ValueError:
            print(f"Please enter a number between 1 and {COLS}.")

def play():
    board = make_board()
    players = ["X", "O"]
    turn = 0

    print("Connect 4!")

    while True:
        print_board(board)
        player = players[turn % 2]
        col = get_move(player)

        if drop_piece(board, col, player) == -1:
            print("That column is full. Try another.")
            continue

        if check_winner(board, player):
            print_board(board)
            print(f"\nPlayer {player} wins!")
            break
        if is_full(board):
            print_board(board)
            print("\nIt's a draw!")
            break

        turn += 1

play()
