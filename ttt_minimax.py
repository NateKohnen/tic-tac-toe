class MinimaxAlgorithm:
    def __init__(self, player):
        self.player = player

    def make_move(self, game):
        _, move = self.minimax(game)
        return move

    def minimax(self, game):
        if game.is_game_over():
            score = self.evaluate_board(game)
            return score, None

        scores = []
        moves = []

        for move in self.get_available_moves(game):
            game_copy = game.copy()  # Create a copy to simulate the move
            game_copy.make_move(move)

            next_player = 'O' if self.player == 'X' else 'X'
            score, _ = self.minimax(game_copy)

            scores.append(score)
            moves.append(move)

        if self.player == 'X':
            # Maximize score for 'X' player
            best_score_index = scores.index(max(scores))
        else:
            # Minimize score for 'O' player
            best_score_index = scores.index(min(scores))

        return scores[best_score_index], moves[best_score_index]

    def evaluate_board(self, game):
        winner = game.get_winner()

        if winner == self.player:
            return 10
        elif winner is not None and winner != self.player:
            return -10
        else:
            return 0

    def get_available_moves(self, game):
        return [i for i, val in enumerate(game.get_board()) if val == ' ']
