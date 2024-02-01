import random

def make_move(game):
    # Get a list of available positions on the board
    available_positions = [i for i, val in enumerate(game.get_board()) if val == ' ']

    if available_positions:
        # Choose a random available position
        random_position = random.choice(available_positions)
        print(f"Random Algorithm 1 chooses position {random_position}")
        return random_position
    else:
        print("No available moves.")
        return -1
