# CS4750 HW4 Group 32

def evaluate_board(board):
    """
    Evaluate the board state by counting specific patterns.
    Also detects if either player has an imminent winning move.
    :param board: The current game board (5x6 grid).
    :return: A heuristic score based on pattern detection or immediate win detection.
    """
    # Check if Player 1 (X) has a winning move
    if has_imminent_win(board, 'X'):
        return float('inf')  # Player 1 should win, return maximum value
    
    # Check if Player 2 (0) has a winning move
    if has_imminent_win(board, 'O'):
        return -float('inf')  # Player 2 should win, return minimum value

    # Otherwise, calculate the heuristic score based on patterns
    score = 0
    score += 200 * count_two_side_open_3_in_a_row(board, 'X') - 80 * count_two_side_open_3_in_a_row(board, 'O')
    score += 150 * count_one_side_open_3_in_a_row(board, 'X') - 40 * count_one_side_open_3_in_a_row(board, 'O')
    score += 20 * count_two_side_open_2_in_a_row(board, 'X') - 15 * count_two_side_open_2_in_a_row(board, 'O')
    score += 5 * count_one_side_open_2_in_a_row(board, 'X') - 2 * count_one_side_open_2_in_a_row(board, 'O')
    return score

def has_imminent_win(board, player):
    """
    Check if the given player has an imminent win (a 4-in-a-row).
    :param board: The current game board.
    :param player: The player ('X' or 'O') to check for an imminent win.
    :return: True if the player has a 4-in-a-row, otherwise False.
    """
    # Check horizontal wins
    for row in range(5):
        for col in range(3):  # Check up to column 3 to avoid out of bounds
            if board[row][col] == player and board[row][col + 1] == player and board[row][col + 2] == player and board[row][col + 3] == player:
                return True
    
    # Check vertical wins
    for col in range(6):
        for row in range(2):  # Check up to row 2 to avoid out of bounds
            if board[row][col] == player and board[row + 1][col] == player and board[row + 2][col] == player and board[row + 3][col] == player:
                return True
    
    # Check diagonal (bottom-left to top-right)
    for row in range(2):
        for col in range(3):
            if board[row][col] == player and board[row + 1][col + 1] == player and board[row + 2][col + 2] == player and board[row + 3][col + 3] == player:
                return True

    # Check diagonal (top-left to bottom-right)
    for row in range(3, 5):
        for col in range(3):
            if board[row][col] == player and board[row - 1][col + 1] == player and board[row - 2][col + 2] == player and board[row - 3][col + 3] == player:
                return True
    
    return False

def is_one_side_open(board, row, col, direction, length, player):
    """
    Check if a sequence is one-side-open (one end of the sequence is open).
    :param board: The current game board.
    :param row: Starting row of the sequence.
    :param col: Starting column of the sequence.
    :param direction: The direction of the sequence (horizontal, vertical, diagonal1, diagonal2).
    :param length: The length of the sequence to check.
    :param player: The player ('X' or 'O') for whom the sequence is being checked.
    :return: True if the sequence is one-side-open, False otherwise.
    """
    if direction == 'horizontal' and col + length - 1 < len(board[0]) and all(board[row][col + i] == player for i in range(length)):
        return (col - 1 >= 0 and board[row][col - 1] == ' ') or (col + length < len(board[0]) and board[row][col + length] == ' ')
    if direction == 'vertical' and row + length - 1 < len(board) and all(board[row + i][col] == player for i in range(length)):
        return (row - 1 >= 0 and board[row - 1][col] == ' ') or (row + length < len(board) and board[row + length][col] == ' ')
    if direction == 'diagonal1' and row + length - 1 < len(board) and col + length - 1 < len(board[0]) and all(board[row + i][col + i] == player for i in range(length)):
        return (row - 1 >= 0 and col - 1 >= 0 and board[row - 1][col - 1] == ' ') or (row + length < len(board) and col + length < len(board[0]) and board[row + length][col + length] == ' ')
    if direction == 'diagonal2' and row - length + 1 >= 0 and col + length - 1 < len(board[0]) and all(board[row - i][col + i] == player for i in range(length)):
        return (row + 1 < len(board) and col - 1 >= 0 and board[row + 1][col - 1] == ' ') or (row - length >= 0 and col + length < len(board[0]) and board[row - length][col + length] == ' ')
    return False

def is_two_side_open(board, row, col, direction, length, player):
    """
    Check if a sequence is two-side-open (both ends of the sequence are open).
    :param board: The current game board.
    :param row: Starting row of the sequence.
    :param col: Starting column of the sequence.
    :param direction: The direction of the sequence.
    :param length: The length of the sequence to check.
    :param player: The player ('X' or 'O') for whom the sequence is being checked.
    :return: True if the sequence is two-side-open, False otherwise.
    """
    if direction == 'horizontal' and col + length - 1 < len(board[0]) and all(board[row][col + i] == player for i in range(length)):
        return col - 1 >= 0 and col + length < len(board[0]) and board[row][col - 1] == ' ' and board[row][col + length] == ' '
    if direction == 'vertical' and row + length - 1 < len(board) and all(board[row + i][col] == player for i in range(length)):
        return row - 1 >= 0 and row + length < len(board) and board[row - 1][col] == ' ' and board[row + length][col] == ' '
    if direction == 'diagonal1' and row + length - 1 < len(board) and col + length - 1 < len(board[0]) and all(board[row + i][col + i] == player for i in range(length)):
        return row - 1 >= 0 and col - 1 >= 0 and row + length < len(board) and col + length < len(board[0]) and board[row - 1][col - 1] == ' ' and board[row + length][col + length] == ' '
    if direction == 'diagonal2' and row - length + 1 >= 0 and col + length - 1 < len(board[0]) and all(board[row - i][col + i] == player for i in range(length)):
        return row + 1 < len(board) and col - 1 >= 0 and row - length >= 0 and col + length < len(board[0]) and board[row + 1][col - 1] == ' ' and board[row - length][col + length] == ' '
    return False

def count_one_side_open_3_in_a_row(board, player):
    """
    Count the number of one-side-open 3-in-a-row patterns for the given player.
    """
    count = 0
    for row in range(5):
        for col in range(6):
            if is_one_side_open(board, row, col, 'horizontal', 3, player): count += 1
            if is_one_side_open(board, row, col, 'vertical', 3, player): count += 1
            if is_one_side_open(board, row, col, 'diagonal1', 3, player): count += 1
            if is_one_side_open(board, row, col, 'diagonal2', 3, player): count += 1
    return count

def count_two_side_open_3_in_a_row(board, player):
    """
    Count the number of two-side-open 3-in-a-row patterns for the given player.
    """
    count = 0
    for row in range(5):
        for col in range(6):
            if is_two_side_open(board, row, col, 'horizontal', 3, player): count += 1
            if is_two_side_open(board, row, col, 'vertical', 3, player): count += 1
            if is_two_side_open(board, row, col, 'diagonal1', 3, player): count += 1
            if is_two_side_open(board, row, col, 'diagonal2', 3, player): count += 1
    return count

def count_one_side_open_2_in_a_row(board, player):
    """
    Count the number of one-side-open 2-in-a-row patterns for the given player.
    """
    count = 0
    for row in range(5):
        for col in range(6):
            if is_one_side_open(board, row, col, 'horizontal', 2, player): count += 1
            if is_one_side_open(board, row, col, 'vertical', 2, player): count += 1
            if is_one_side_open(board, row, col, 'diagonal1', 2, player): count += 1
            if is_one_side_open(board, row, col, 'diagonal2', 2, player): count += 1
    return count

def count_two_side_open_2_in_a_row(board, player):
    """
    Count the number of two-side-open 2-in-a-row patterns for the given player.
    """
    count = 0
    for row in range(5):
        for col in range(6):
            if is_two_side_open(board, row, col, 'horizontal', 2, player): count += 1
            if is_two_side_open(board, row, col, 'vertical', 2, player): count += 1
            if is_two_side_open(board, row, col, 'diagonal1', 2, player): count += 1
            if is_two_side_open(board, row, col, 'diagonal2', 2, player): count += 1
    return count
