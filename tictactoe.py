def print_board(board):
    for i, row in enumerate(board):
        print(" | ".join(row))
        if i < 2:
            print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def get_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if 0 <= move <= 8 and board[row][col] == " ":
                return row, col
            else:
                print("Invalid move. Try again.")
        except (ValueError, IndexError):
            print("Please enter a number between 1 and 9.")

def play():
    board = [[" "] * 3 for _ in range(3)]
    players = ["X", "O"]
    turn = 0

    print("Tic-Tac-Toe!")
    print("Positions: 1-9 (left to right, top to bottom)\n")

    while True:
        print_board(board)
        player = players[turn % 2]
        row, col = get_move(board, player)
        board[row][col] = player

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
