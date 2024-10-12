# CS4750 HW4 Group 32

from game import initialize_board, print_board, is_terminal_state
from player import minimax_move 
from player import make_move 
import time  # Import time module to measure execution time for each move


def play_game():
    """
    Main loop to manage the game between Player X and Player O.
    Alternates turns between players until the game reaches a terminal state (win, lose, or tie).
    """
    # Initialize the game board with the starting positions for player 1 and 2
    board = initialize_board()
    move_count = 0  # Tracker for the number of moves made

    # Loop until the game reaches a terminal state (win, lose, or tie)
    while True:
        print("=" * 30)  # Separator for clarity between moves
        print_board(board)  # Print the current state of the board to see
        start_time = time.time()  # Record the start time to measure move execution

        if move_count % 2 == 0:  # Player 1's turn (X)
            print(f"Move {move_count + 1}: Player 1's turn")
            move, node_count = minimax_move(board, 2, 'X')  # Get the best move using minimax with depth 2
        else:  # Player 2's turn (0)
            print(f"Move {move_count + 1}: Player 2's turn")
            move, node_count = minimax_move(board, 4, 'O')  # Get the best move using minimax with depth 4

        # Apply the selected move to the board
        board = make_move(board, move, 'X' if move_count % 2 == 0 else 'O')

        # Convert the 0-based move to 1-based indexing for printing
        row_1_based = move[0] + 1
        col_1_based = move[1] + 1

        print(f"Move {move_count + 1}: Player {'1' if move_count % 2 == 0 else '2'} played ({row_1_based}, {col_1_based})")
        print(f"Nodes generated: {node_count}") 
        end_time = time.time()  # Record the end time after the move is made
        print(f"Time taken: {end_time - start_time} seconds\n")

        # Check if the game has ended
        winner = is_terminal_state(board)
        if winner:
            break  # Exit the loop if there is a winner or tie

        move_count += 1  # Increment move count to switch turns between players

    # Game Over message and final board display
    print("Game is Over!")
    print("=" * 30)  # End of game separator
    print_board(board)  # Print the final board state when the game ends

    # Announce the result
    if winner == 'X':
        print("Player 1 (X) wins!")
    elif winner == 'O':
        print("Player 2 (O) wins!")
    else:
        print("It's a tie!")


if __name__ == '__main__':
    play_game()  # Start the game when running this file
