PLAYER, BOT = 'X', 'O'
GRID_SIZE = 3

# This function returns True if playable moves remain
# It returns False otherwise
def remaining_moves(b):
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if b[i][j] == "_":
                return True
    return False

# Evaluates the board for winning sequences
def evaluate(b):

    # Check all rows for winning sequence
    for row in range(GRID_SIZE):
        if b[row][0] == b[row][1] and b[row][1] == b[row][2]:
            if b[row][0] == PLAYER:
                return -10
            elif b[row][0] == BOT:
                return 10

    # Check all columns for winning sequence
    for col in range(GRID_SIZE):
        if b[0][col] == b[1][col] and b[1][col] == b[2][col]:
            if b[0][col] == PLAYER:
                return -10
            elif b[0][col] == BOT:
                return 10

    # Check both diagonals for winning sequence
    if b[0][0] == b[1][1] and b[1][1] == b[2][2]:
        if b[1][1] == PLAYER:
            return -10
        elif b[1][1] == BOT:
            return 10

    if b[0][2] == b[1][1] and b[1][1] == b[2][0]:
        if b[1][1] == PLAYER:
            return -10
        elif b[1][1] == BOT:
            return 10

    # If no winning sequence is detected, return 0
    return 0

# Evaluates all possible resulting positions from current board state
def minimax(b, depth, is_max):
    score = evaluate(b)

    # Return score if the BOT has won
    if score == 10:
        return score

    # Return score if the PLAYER has won
    if score == -10:
        return score

    # Return 0 if there are no moves remaining AND no winner
    if not remaining_moves(b):
        return 0

    # When it is the BOT's move...
    if is_max:
        best = -1000

        # Traverse all cells
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):

                # Check if this is a legal move
                if b[i][j] == '_':

                    # Make the move
                    b[i][j] = BOT

                    # Call minimax recursively and store the best outcome
                    best = max(best, minimax(b, depth + 1, not is_max))

                    # Undo the move
                    b[i][j] = '_'

        return best

    # When it is the PLAYER's move...
    else:
        best = 1000

        # Traverse all cells
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):

                # Check if this is a legal move
                if b[i][j] == '_':

                    # Make the move
                    b[i][j] = PLAYER

                    # Call minimax recursively and store the best outcome
                    best = min(best, minimax(b, depth + 1, not is_max))

                    # Undo the move
                    b[i][j] = '_'

        return best

# Returns the best possible move for the BOT
def find_best_move(b):
    best_val = -1000
    best_move = (-1, -1)

    # Evaluate all legal moves, return cell with optimal minimax value
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):

            # Check if this is a legal move
            if b[i][j] == '_':

                # Make the move
                b[i][j] = BOT

                # Store the minimax value of the move
                move_val = minimax(b, 0, False)

                # Undo the move
                b[i][j] = '_'

                # If the value of the move just analyzed is greater than
                # the best value, update best_val and store the move coordinates
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    print("The value of the best move is:", best_val)
    return best_move

# Gamestate
board = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['_', '_', '_']
]

bestMove = find_best_move(board)

print("The optimal move is:", bestMove[0], bestMove[1])
