# CS4750 HW4 Group 32

def initialize_board():
    """
    Initialize the game board as a 5x6 grid with empty spaces. 
    Place the first moves for Player 1 (X) and Player 2 (O).
    """
    board = [[' ' for _ in range(6)] for _ in range(5)]
    board[2][3] = 'X'  # Player 1 starts at (3, 4) (1-based indexing)
    board[2][2] = 'O'  # Player 2 starts at (3, 3) (1-based indexing)
    return board

def print_board(board):
    """
    Print the current state of the game board with 1-based row and column numbers.
    """
    print("   " + " ".join(str(col + 1) for col in range(6)))
    for row_idx, row in enumerate(board):
        print(f"{row_idx + 1}  " + ' '.join(row))
    print()

def is_terminal_state(board):
    """
    Check if the game has reached a terminal state (win, lose, or tie):
    - Return 'X' or 'O' if a player wins by aligning four in a row.
    - Return 'Tie' if the board is full with no winner.
    - Return None if the game is still ongoing.
    """
    for row in range(5):
        for col in range(3):
            if board[row][col] != ' ' and board[row][col] == board[row][col + 1] == board[row][col + 2] == board[row][col + 3]:
                return board[row][col]  # Horizontal win
    
    for col in range(6):
        for row in range(2):
            if board[row][col] != ' ' and board[row][col] == board[row + 1][col] == board[row + 2][col] == board[row + 3][col]:
                return board[row][col]  # Vertical win

    for row in range(2):
        for col in range(3):
            if board[row][col] != ' ' and board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] == board[row + 3][col + 3]:
                return board[row][col]  # Diagonal (bottom-left to top-right)

    for row in range(3, 5):
        for col in range(3):
            if board[row][col] != ' ' and board[row][col] == board[row - 1][col + 1] == board[row - 2][col + 2] == board[row - 3][col + 3]:
                return board[row][col]  # Diagonal (top-left to bottom-right)

    for row in board:
        if ' ' in row:
            return None  # Board not full, game continues

    return 'Tie'  # Board full, game ends in tie

def play_game():
    """
    Main loop to manage the game between Player 1 (X) and Player 2 (O).
    Alternates turns until the game reaches a terminal state.
    """
    from player import minimax_move, make_move

    board = initialize_board()
    move_count = 0

    while True:
        print_board(board)

        if move_count % 2 == 0:
            print("Player 1's turn (X)")
            move, node_count = minimax_move(board, 2, 'X')
        else:
            print("Player 2's turn (O)")
            move, node_count = minimax_move(board, 4, 'O')

        board = make_move(board, move, 'X' if move_count % 2 == 0 else 'O')

        result = is_terminal_state(board)
        if result:
            break

        move_count += 1

    print_board(board)
    if result == 'X':
        print("Player 1 (X) wins!")
    elif result == 'O':
        print("Player 2 (O) wins!")
    else:
        print("It's a tie!")

if __name__ == '__main__':
    play_game()
