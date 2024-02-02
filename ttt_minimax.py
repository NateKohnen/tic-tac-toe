from math import inf

class MinimaxAlgorithm:
    def __init__(self, player, max_depth=9):
        self.player = player
        self.max_depth = max_depth
        self.position_counter = 0  # Counter to track the number of positions analyzed

    def make_move(self, game):
        self.position_counter = 0
        _, move = self.minimax(game, 0)
        return move

    def minimax(self, game, depth):
        if depth == self.max_depth or game.is_game_over():
            score = self.evaluate_board(game, depth)
            return score, None

        # Initialize best_score based on the player
        best_score = -inf if self.player == 'X' else inf

        moves_and_scores = []

        for move in self.get_available_moves(game):
            game_copy = game.copy()  # Create a copy to simulate the move
            game_copy.make_move(move)

            score, _ = self.minimax(game_copy, depth + 1)

            moves_and_scores.append((score, move))

            # Increment the position counter
            self.position_counter += 1

        if not moves_and_scores:
            # No available moves
            return -inf if self.player == 'X' else inf, None

        if self.player == 'X':
            # Maximize score for 'X' player
            best_score, best_move = max(moves_and_scores, key=lambda x: x[0])
        else:
            # Minimize score for 'O' player
            best_score, best_move = min(moves_and_scores, key=lambda x: x[0])

        return best_score, best_move

    def evaluate_board(self, game, depth):
        winner = game.get_winner()

        if winner == self.player:
            return 10 - depth
        elif winner is not None and winner != self.player:
            return -10 + depth
        else:
            return 0

    def get_available_moves(self, game):
        available_moves = [i for i, val in enumerate(game.get_board()) if val == ' ']

        # Return available_moves if there are any, otherwise return [0]
        return sorted(available_moves) if available_moves else [0]
