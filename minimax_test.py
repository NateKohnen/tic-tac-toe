from tictactoegame import TicTacToeGame
from ttt_minimax import MinimaxAlgorithm

# Initialize game
game = TicTacToeGame(3)

# Initialize Minimax algorithm
algorithm = MinimaxAlgorithm(player='X')

def print_tic_tac_toe_board(board):
    for i in range(0, len(board), 3):
        row = board[i:i + 3]
        print(" | ".join(row))
        if i < len(board) - 3:
            print("-" * 9)
    print()

# Make moves until the game is over
while not game.is_game_over():
    # Print the current state of the board
    print_tic_tac_toe_board(game.get_board())

    # Print the position counter
    print(f"Position Counter: {algorithm.position_counter}")

    # Make a move using Minimax
    position = algorithm.make_move(game)

    # Apply the move to the game
    game.make_move(position)

# Print the final state of the board
print("Final Board State:")
print_tic_tac_toe_board(game.get_board())
