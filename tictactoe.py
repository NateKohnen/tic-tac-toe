# CONSTANTS
OLD, NEW = 'X', 'O'
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
            if b[row][0] == OLD:
                return -1
            elif b[row][0] == NEW:
                return 1

    # Check all columns for winning sequence
    for col in range(GRID_SIZE):
        if b[0][col] == b[1][col] and b[1][col] == b[2][col]:
            if b[0][col] == OLD:
                return -1
            elif b[0][col] == NEW:
                return 1

    # Check both diagonals for winning sequence
    if b[0][0] == b[1][1] and b[1][1] == b[2][2]:
        if b[1][1] == OLD:
            return -1
        elif b[1][1] == NEW:
            return 1

    if b[0][2] == b[1][1] and b[1][1] == b[2][0]:
        if b[1][1] == OLD:
            return -1
        elif b[1][1] == NEW:
            return 1

    # If no winning sequence is detected, return 0
    return 0

def main():
    # Initialize gamestate
    player_turn = True
    board = [['_' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

    while True:
        if player_turn:

        elif not player_turn:


        # Check for game over conditions
        if not remaining_moves(board) or evaluate(board) != 0:


if __name__ == "__main__":
    main()
