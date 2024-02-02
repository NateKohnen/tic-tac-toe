from tictactoegame import TicTacToeGame
from ttt_minimax import MinimaxAlgorithm
from ttt_random1 import make_move as random_algorithm_move

def run_tournament(number_of_iterations=1):
    algorithm_a_wins = 0
    algorithm_b_wins = 0
    draws = 0

    starting_player = 'X'

    for _ in range(number_of_iterations):
        # Initialize the game with the starting player
        game = TicTacToeGame()
        game.current_player = starting_player

        # Use MinimaxAlgorithm for Algorithm A
        algorithm_a = MinimaxAlgorithm(starting_player)

        # Use random algorithm for Algorithm B
        algorithm_b_move = random_algorithm_move

        while not game.is_game_over():
            # Make moves using Algorithm A and B alternatively
            if game.current_player == 'X':
                position = algorithm_a.make_move(game)
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

        # Switch the starting player for the next game
        starting_player = 'O' if starting_player == 'X' else 'X'

    # Print the tournament results
    print(f"Results after {number_of_iterations} iterations:")
    print(f"Algorithm A (Minimax) wins: {algorithm_a_wins}")
    print(f"Algorithm B (Random) wins: {algorithm_b_wins}")
    print(f"Draws: {draws}")

if __name__ == "__main__":
    run_tournament()
