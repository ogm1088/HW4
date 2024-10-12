# CS4750 HW4 Group 32

from heuristic import evaluate_board 

def minimax_move(board, depth, player):
    """
    Determine the best move for the given player using minimax with Alpha-Beta pruning.
    Tracks the number of nodes generated during the search.
    """
    node_count = [0]
    best_move, _ = minimax(board, depth, True, player, node_count, float('-inf'), float('inf'))
    return best_move, node_count[0]

def minimax(board, depth, is_maximizing, player, node_count, alpha, beta):
    """
    Recursive minimax with Alpha-Beta pruning to explore the game tree and determine the optimal move.
    """
    from game import is_terminal_state
    node_count[0] += 1

    if depth == 0 or is_terminal_state(board):
        return None, evaluate_board(board)

    best_move = None

    if is_maximizing:
        max_eval = float('-inf')
        possible_moves = sorted(get_all_possible_moves(board, player), key=lambda move: (move[1], move[0]))

        for move in possible_moves:
            new_board = make_move([row[:] for row in board], move, player)
            _, eval = minimax(new_board, depth - 1, False, 'O', node_count, alpha, beta)
            if eval > max_eval:
                max_eval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break

        return best_move, max_eval

    else:
        min_eval = float('inf')
        possible_moves = sorted(get_all_possible_moves(board, 'O'), key=lambda move: (move[1], move[0]))

        for move in possible_moves:
            new_board = make_move([row[:] for row in board], move, 'O')
            _, eval = minimax(new_board, depth - 1, True, 'X', node_count, alpha, beta)
            if eval < min_eval:
                min_eval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break

        return best_move, min_eval

def get_all_possible_moves(board, player):
    """
    Generate all possible valid moves for the player.
    A move is valid if it is an empty space adjacent to an existing piece.
    """
    possible_moves = [(row, col) for row in range(5) for col in range(6) if board[row][col] == ' ' and is_adjacent_to_piece(board, row, col)]
    return possible_moves

def is_adjacent_to_piece(board, row, col):
    """
    Check if a given empty space is adjacent to any piece ('X' or 'O').
    """
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    return any(0 <= row + d_row < 5 and 0 <= col + d_col < 6 and board[row + d_row][col + d_col] in ['X', 'O'] for d_row, d_col in directions)

def make_move(board, move, player):
    """
    Apply a move to the board by placing the player's piece at the specified location.
    """
    row, col = move
    if board[row][col] == ' ':
        board[row][col] = player
    return board
