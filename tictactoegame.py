class TicTacToeGame:
    def __init__(self):
        self.board = [' '] * 9  # Represents the Tic-Tac-Toe board
        self.current_player = 'X'  # Starting player
        self.winner = None  # 'X', 'O', or None
        self.game_over = False  # Flag to indicate if the game is over

    def make_move(self, position):
        # Make a move on the board
        if not self.game_over and 0 <= position < 9 and self.board[position] == ' ':
            self.board[position] = self.current_player
            if self._check_winner():
                self.winner = self.current_player
                self.game_over = True
            elif ' ' not in self.board:
                # The board is full, and there is no winner (a draw)
                self.game_over = True
            else:
                # Switch to the other player for the next move
                self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            print("Invalid move. Try again.")

    def _check_winner(self):
        # Check if the current player is the winner
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]  # Diagonals
        ]

        for combo in winning_combinations:
            if (
                self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]]
                and self.board[combo[0]] != ' '
            ):
                return True

        return False

    def get_board(self):
        # Return a copy of the current state of the board
        return self.board.copy()

    def is_game_over(self):
        # Return True if the game is over (either a winner or a draw)
        return self.game_over

    def get_winner(self):
        # Return the winner ('X', 'O') or None if there is no winner
        return self.winner
