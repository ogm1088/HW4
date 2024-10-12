# Function to initialize the board with empty spaces and place the first moves for both players
def initialize_board():
    """
    Initialize the game board as a 5x6 grid filled with empty spaces. 
    Place the first moves for Player X and Player O.
    """
    # Create a 5x6 board represented as a 2D list filled with empty spaces
    board = [[' ' for _ in range(6)] for _ in range(5)]
    
    # Initial moves for Player X and Player O using 0-based indexing
    board[2][3] = 'X'  # Player X starts at position (3, 4) in 1-based indexing
    board[2][2] = 'O'  # Player O starts at position (3, 3) in 1-based indexing
    
    return board

# Function to print the current state of the board with row and column numbers (1-based index)
def print_board(board):
    """
    Print the current state of the game board in a readable format with 1-based row and column numbers.
    """
    # Print column numbers (1-based indexing)
    print("   " + " ".join(str(col + 1) for col in range(6)))  # Print 1-based column numbers

    # Print each row with row numbers (1-based indexing)
    for row_idx, row in enumerate(board):
        print(f"{row_idx + 1}  " + ' '.join(row))  # Print 1-based row numbers alongside row contents
    print()  # Add an empty line for better readability

# Function to check if the game has reached a terminal state (win, lose, or tie)
def is_terminal_state(board):
    """
    Check if the game has reached a terminal state:
    - A player wins if they have 4 consecutive 'X' or 'O' in a row (horizontal, vertical, or diagonal).
    - The game is a tie if the board is full with no winner.
    """
    # Check horizontal wins (4 consecutive marks horizontally)
    for row in range(5):
        for col in range(3):  # Only check up to col 3 to avoid out of bounds
            if board[row][col] != ' ' and board[row][col] == board[row][col + 1] == board[row][col + 2] == board[row][col + 3]:
                return True  # There's a 4-in-a-row horizontally
    
    # Check vertical wins (4 consecutive marks vertically)
    for col in range(6):
        for row in range(2):  # Only check up to row 2 to avoid out of bounds
            if board[row][col] != ' ' and board[row][col] == board[row + 1][col] == board[row + 2][col] == board[row + 3][col]:
                return True  # There's a 4-in-a-row vertically

    # Check diagonal wins (bottom-left to top-right)
    for row in range(2):  # Only check up to row 2 to avoid out of bounds
        for col in range(3):  # Only check up to col 3 to avoid out of bounds
            if board[row][col] != ' ' and board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] == board[row + 3][col + 3]:
                return True  # There's a 4-in-a-row diagonally (bottom-left to top-right)

    # Check diagonal wins (top-left to bottom-right)
    for row in range(3, 5):  # Only check rows 3 and 4 to avoid out of bounds
        for col in range(3):  # Only check up to col 3 to avoid out of bounds
            if board[row][col] != ' ' and board[row][col] == board[row - 1][col + 1] == board[row - 2][col + 2] == board[row - 3][col + 3]:
                return True  # There's a 4-in-a-row diagonally (top-left to bottom-right)

    # Check for a tie (if the board is full and no winner)
    for row in board:
        if ' ' in row:
            return False  # The board isn't full yet, so no tie

    return True  # The board is full, and there are no more valid moves, so it's a tie
