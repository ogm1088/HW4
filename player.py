# CS4750 HW4 Group 32

from heuristic import evaluate_board 

# Function to determine the best move using the minimax algorithm with Alpha-Beta pruning
def minimax_move(board, depth, player):
    """
    Function to determine the best move for the given player using the minimax algorithm with Alpha-Beta pruning.
    Also tracks the number of nodes generated during the minimax search.
    
    :param board: Current state of the board.
    :param depth: Maximum depth of the game tree to explore.
    :param player: The current player ('X' or 'O').
    :return: The best move (row, col) for the player and the number of nodes generated.
    """
    node_count = [0]  # Initialize node count (using a list for mutability)

    if player == 'X':
        best_move, _ = minimax(board, depth, True, 'X', node_count, float('-inf'), float('inf'))  # Player X is maximizing
    else:
        best_move, _ = minimax(board, depth, True, 'O', node_count, float('-inf'), float('inf'))  # Player O is maximizing
    
    return best_move, node_count[0]  # Return the best move and the number of nodes generated

# Recursive minimax algorithm with Alpha-Beta pruning
def minimax(board, depth, is_maximizing, player, node_count, alpha, beta):
    """
    Minimax recursive function with Alpha-Beta pruning to explore the game tree and determine the optimal move.
    :param board: Current state of the board.
    :param depth: Remaining depth to explore.
    :param is_maximizing: Boolean to determine if it's the maximizing player's turn.
    :param player: The current player ('X' or 'O').
    :param node_count: A mutable counter for tracking the number of nodes generated.
    :param alpha: Alpha value for Alpha-Beta pruning (best option for the maximizer).
    :param beta: Beta value for Alpha-Beta pruning (best option for the minimizer).
    :return: A tuple of (best_move, evaluation score).
    """
    # Import is_terminal_state only when the function is called, to avoid circular import
    from game import is_terminal_state
    
    # Increment node count for each recursive call
    node_count[0] += 1

    # Base case: If we reach the max depth or terminal state (win, lose, or tie)
    if depth == 0 or is_terminal_state(board):
        return None, evaluate_board(board)  # Return board evaluation score

    if is_maximizing:
        max_eval = float('-inf')  # Initialize to negative infinity for maximizing
        best_move = None
        possible_moves = get_all_possible_moves(board, player)

        # Sort moves to prioritize smaller columns and then smaller rows (tie-breaking)
        possible_moves.sort(key=lambda move: (move[1], move[0]))  # Sort by column, then row

        for move in possible_moves:
            new_board = make_move([row[:] for row in board], move, player)
            _, eval = minimax(new_board, depth - 1, False, 'O', node_count, alpha, beta)  # Minimize opponent
            if eval > max_eval:
                max_eval = eval
                best_move = move  # Update best move with the highest eval
            alpha = max(alpha, eval)
            if beta <= alpha:  # Alpha-Beta pruning
                break

        return best_move, max_eval  # Return the best move and the highest evaluation score

    else:
        min_eval = float('inf')  # Initialize to positive infinity for minimizing
        best_move = None
        possible_moves = get_all_possible_moves(board, 'O')

        # Sort moves to prioritize smaller columns and then smaller rows (tie-breaking)
        possible_moves.sort(key=lambda move: (move[1], move[0]))  # Sort by column, then row

        for move in possible_moves:
            new_board = make_move([row[:] for row in board], move, 'O')
            _, eval = minimax(new_board, depth - 1, True, 'X', node_count, alpha, beta)  # Maximize opponent
            if eval < min_eval:
                min_eval = eval
                best_move = move  # Update best move with the lowest eval
            beta = min(beta, eval)
            if beta <= alpha:  # Alpha-Beta pruning
                break

        return best_move, min_eval  # Return the best move and the lowest evaluation score

# Function to generate all possible valid moves for a player
def get_all_possible_moves(board, player):
    """
    Generate all possible valid moves for the player. A move is valid if it is an empty space
    adjacent to an existing piece ('X' or 'O').
    :param board: The current state of the board.
    :param player: The current player ('X' or 'O').
    :return: A list of possible moves [(row, col), ...].
    """
    possible_moves = []

    # Loop through the board to find empty spaces
    for row in range(5):
        for col in range(6):
            if board[row][col] == ' ':  # Check if the space is empty
                # Check if the empty space is adjacent to an existing piece
                if is_adjacent_to_piece(board, row, col):
                    possible_moves.append((row, col))  # Add the valid move to the list

    return possible_moves  # Return the list of possible moves

# Helper function to check if a position is adjacent to an existing piece ('X' or 'O')
def is_adjacent_to_piece(board, row, col):
    """
    Check if a given empty space is adjacent to any piece ('X' or 'O') in one of the 8 directions.
    :param board: The current state of the board.
    :param row: The row index of the empty space.
    :param col: The column index of the empty space.
    :return: True if adjacent to a piece, False otherwise.
    """
    # Define the 8 possible directions (up, down, left, right, and 4 diagonals)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]

    # Check each direction for adjacency to a piece
    for d_row, d_col in directions:
        adj_row = row + d_row
        adj_col = col + d_col

        # Ensure the adjacent position is within bounds and contains a piece ('X' or 'O')
        if 0 <= adj_row < 5 and 0 <= adj_col < 6 and board[adj_row][adj_col] in ['X', 'O']:
            return True  # An adjacent piece is found

    return False  # No adjacent piece is found

# Function to apply a move to the board
def make_move(board, move, player):
    """
    Apply a move to the board by placing the player's piece at the specified location.
    :param board: The current state of the board.
    :param move: The move (row, col) to be applied.
    :param player: The player making the move ('X' or 'O').
    :return: The updated board with the move applied.
    """
    row, col = move  # Unpack the move into row and column
    # Ensure the move is applied only if the spot is empty
    if board[row][col] == ' ':
        board[row][col] = player  # Place the player's piece on the board
    return board  # Return the updated board
