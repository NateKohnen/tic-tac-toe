class MinimaxAlgorithm:
    def __init__(self, player, max_depth=9):
        self.player = player
        self.max_depth = max_depth

    def make_move(self, game):
        _, move = self.minimax(game, 0)
        return move

    def minimax(self, game, depth):
        if depth == self.max_depth or game.is_game_over():
            score = self.evaluate_board(game, depth)
            return score, None

        scores = []

        for move in self.get_available_moves(game):
            game_copy = game.copy()  # Create a copy to simulate the move
            game_copy.make_move(move)

            next_player = 'O' if self.player == 'X' else 'X'
            score, _ = self.minimax(game_copy, depth + 1)

            scores.append(score)

        if self.player == 'X':
            # Maximize score for 'X' player
            best_score = max(scores)
            best_score_index = scores.index(best_score)
        else:
            # Minimize score for 'O' player
            best_score = min(scores)
            best_score_index = scores.index(best_score)

        return best_score, self.get_available_moves(game)[best_score_index]

    def evaluate_board(self, game, depth):
        winner = game.get_winner()

        if winner == self.player:
            return 10 - depth
        elif winner is not None and winner != self.player:
            return -10 + depth
        else:
            return 0

    def get_available_moves(self, game):
        return [i for i, val in enumerate(game.get_board()) if val == ' ']
