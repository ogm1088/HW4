# CS4750 HW4 Group 32

# Function to initialize the board as a 5x6 grid with empty spaces.
# This also places the first moves for both players.
def initialize_board():
    """
    Initialize the game board as a 5x6 grid filled with empty spaces. 
    Place the first moves for Player 1 (X) and Player 2 (O).
    """
    # Create a 5x6 board represented as a 2D list filled with empty spaces
    board = [[' ' for _ in range(6)] for _ in range(5)]
    
    # Initial moves for Player 1 (X) and Player 2 (O) using 0-based indexing
    board[2][3] = 'X'  # Player 1 starts at position (3, 4) in 1-based indexing
    board[2][2] = 'O'  # Player 2 starts at position (3, 3) in 1-based indexing
    
    return board

# Function to print the current state of the board with row and column numbers (1-based index)
def print_board(board):
    """
    Print the current state of the game board in a readable format with 1-based row and column numbers.
    """
    # Print column numbers (1-based indexing)
    print("   " + " ".join(str(col + 1) for col in range(6)))

    # Print each row with row numbers (1-based indexing)
    for row_idx, row in enumerate(board):
        print(f"{row_idx + 1}  " + ' '.join(row))  # Print 1-based row numbers alongside row contents
    print()  # Add an empty line for better readability


# This function checks if the game has reached a terminal state (win, lose, or tie).
# A player wins if they have 4 consecutive 'X' or 'O' in a row (horizontal, vertical, or diagonal).
# The game is a tie if the board is full with no winner.
def is_terminal_state(board):
    """
    Check if the game has reached a terminal state (win, lose, or tie):
    - A player wins if they have 4 consecutive 'X' or 'O' in a row (horizontal, vertical, or diagonal).
    - The game is a tie if the board is full with no winner.
    :return: 'X' if Player 1 wins, 'O' if Player 2 wins, 'Tie' if it's a tie, or None if the game is not over.
    """
    # Check horizontal wins (4 consecutive marks horizontally)
    for row in range(5):
        for col in range(3):  # Only check up to col 3 to avoid out of bounds
            if board[row][col] != ' ' and board[row][col] == board[row][col + 1] == board[row][col + 2] == board[row][col + 3]:
                return board[row][col]  # Return 'X' or 'O' as the winner
    
    # Check vertical wins (4 consecutive marks vertically)
    for col in range(6):
        for row in range(2):  # Only check up to row 2 to avoid out of bounds
            if board[row][col] != ' ' and board[row][col] == board[row + 1][col] == board[row + 2][col] == board[row + 3][col]:
                return board[row][col]  # Return 'X' or 'O' as the winner

    # Check diagonal wins (bottom-left to top-right)
    for row in range(2):  # Only check up to row 2 to avoid out of bounds
        for col in range(3):  # Only check up to col 3 to avoid out of bounds
            if board[row][col] != ' ' and board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] == board[row + 3][col + 3]:
                return board[row][col]  # Return 'X' or 'O' as the winner

    # Check diagonal wins (top-left to bottom-right)
    for row in range(3, 5):  # Only check rows 3 and 4 to avoid out of bounds
        for col in range(3):  # Only check up to col 3 to avoid out of bounds
            if board[row][col] != ' ' and board[row][col] == board[row - 1][col + 1] == board[row - 2][col + 2] == board[row - 3][col + 3]:
                return board[row][col]  # Return 'X' or 'O' as the winner

    # Check for a tie (if the board is full and no winner)
    for row in board:
        if ' ' in row:
            return None  # The board isn't full yet, so no tie

    return 'Tie'  # The board is full and there are no more valid moves, so it's a tie


# Function to run the game and announce the winner or tie
def play_game():
    """
    Main loop to manage the game between Player 1(X) and Player 2(O).
    Alternates turns between players until the game reaches a terminal state (win, lose, or tie).
    """
    from player import minimax_move, make_move  # Avoid circular import by moving inside the function
    
    board = initialize_board()  # Initialize the game board
    move_count = 0  # Track the number of moves made

    while True:
        print_board(board)  # Display the board

        # Determine whose turn it is
        if move_count % 2 == 0:
            print("Player 1's turn (X)")
            move, node_count = minimax_move(board, 2, 'X')  # Get the best move for Player X
        else:
            print("Player 2's turn (O)")
            move, node_count = minimax_move(board, 4, 'O')  # Get the best move for Player O

        # Apply the move
        board = make_move(board, move, 'X' if move_count % 2 == 0 else 'O')

        # Check if the game has ended
        result = is_terminal_state(board)
        if result:
            break  # Exit the loop if there is a winner or a tie

        move_count += 1  # Increment move count for the next turn

    # Print the final board
    print_board(board)

    # Announce the result
    if result == 'X':
        print("Player 1 (X) wins!")
    elif result == 'O':
        print("Player 2 (O) wins!")
    else:
        print("It's a tie!")


if __name__ == '__main__':
    play_game()  # Start the game when running this file
