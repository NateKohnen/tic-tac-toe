from tictactoegame import TicTacToeGame
from ttt_random1 import make_move as algorithm_a_move
from ttt_random2 import make_move as algorithm_b_move

def run_tournament(number_of_iterations=1):
    algorithm_a_wins = 0
    algorithm_b_wins = 0
    draws = 0

    for _ in range(number_of_iterations):
        # Initialize the game
        game = TicTacToeGame()

        while not game.is_game_over():
            # Make moves using Algorithm A and B alternatively
            if game.current_player == 'X':
                position = algorithm_a_move(game)
                game.make_move(position)
            else:
                position = algorithm_b_move(game)
                game.make_move(position)

        # Record the result of the game
        winner = game.get_winner()
        if winner == 'X':
            algorithm_a_wins += 1
        elif winner == 'O':
            algorithm_b_wins += 1
        else:
            draws += 1
        game.print_board()

    # Print the tournament results
    print(f"Results after {number_of_iterations} iterations:")
    print(f"Algorithm A wins: {algorithm_a_wins}")
    print(f"Algorithm B wins: {algorithm_b_wins}")
    print(f"Draws: {draws}")

if __name__ == "__main__":
    run_tournament()
