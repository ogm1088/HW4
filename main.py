# CS4750 HW4 Group 32

from game import initialize_board, print_board, is_terminal_state
from player import minimax_move, make_move
import time

def play_game():
    """
    Manage the game between Player 1 (X) and Player 2 (O).
    Alternates turns until the game reaches a terminal state (win, lose, or tie).
    """
    board = initialize_board()
    move_count = 0

    while True:
        print("=" * 30)  # Separator for clarity between moves
        print_board(board)

        start_time = time.time()

        if move_count % 2 == 0:
            print(f"Move {move_count + 1}: Player 1's turn")
            move, node_count = minimax_move(board, 2, 'X')
        else:
            print(f"Move {move_count + 1}: Player 2's turn")
            move, node_count = minimax_move(board, 4, 'O')

        board = make_move(board, move, 'X' if move_count % 2 == 0 else 'O')

        row_1_based = move[0] + 1
        col_1_based = move[1] + 1
        print(f"Move {move_count + 1}: Player {'1' if move_count % 2 == 0 else '2'} played ({row_1_based}, {col_1_based})")
        print(f"Nodes generated: {node_count}")
        print(f"Time taken: {time.time() - start_time} seconds\n")

        winner = is_terminal_state(board)
        if winner:
            break

        move_count += 1

    print("Game is Over!")
    print("=" * 30)
    print_board(board)

    if winner == 'X':
        print("Player 1 (X) wins!")
    elif winner == 'O':
        print("Player 2 (O) wins!")
    else:
        print("It's a tie!")

if __name__ == '__main__':
    play_game()
