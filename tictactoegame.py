class TicTacToeGame:
    GRID_SIZE = 3

    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.board = [' '] * (grid_size ** 2)  # Represents the Tic-Tac-Toe board
        self.current_player = 'X'  # Starting player
        self.winner = None  # 'X', 'O', or None
        self.game_over = False  # Flag to indicate if the game is over
        self.winning_combinations = self._generate_winning_combinations()

    def make_move(self, position):
        # Make a move on the board
        if not self.game_over and 0 <= position < len(self.board) and self.board[position] == ' ':
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
        for combo in self.winning_combinations:
            if all(self.board[i] == self.current_player for i in combo):
                return True
        return False

    def _generate_winning_combinations(self):
        # Generate winning combinations based on the grid size
        combinations = []

        # Rows
        for i in range(0, len(self.board), self.grid_size):
            combinations.append(list(range(i, i + self.grid_size)))

        # Columns
        for i in range(self.grid_size):
            combinations.append(list(range(i, len(self.board), self.grid_size)))

        # Diagonals
        combinations.append(list(range(0, len(self.board), self.grid_size + 1)))
        combinations.append(list(range(self.grid_size - 1, len(self.board) - 1, self.grid_size - 1)))

        return combinations

    def get_board(self):
        # Return a copy of the current state of the board
        return self.board.copy()

    def is_game_over(self):
        # Return True if the game is over (either a winner or a draw)
        return self.game_over

    def get_winner(self):
        # Return the winner ('X', 'O') or None if there is no winner
        return self.winner

    def get_grid_size(self):
        # Return the dimensions of the board
        return self.grid_size

    def copy(self):
        # Create a copy of the current game state
        new_game = TicTacToeGame(self.grid_size)
        new_game.board = self.board.copy()
        new_game.current_player = self.current_player
        new_game.winner = self.winner
        new_game.game_over = self.game_over
        return new_game
