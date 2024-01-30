import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
LINE_COLOR = (255, 255, 255)
LINE_WIDTH = 15
GRID_SIZE = 3
SQUARE_SIZE = WIDTH // GRID_SIZE

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Initialize the game board
board = [['' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
current_player = 'X'

# Function to draw the grid
def draw_grid():
    for i in range(1, GRID_SIZE):
        pygame.draw.line(screen, LINE_COLOR, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, HEIGHT), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (0, i * SQUARE_SIZE), (WIDTH, i * SQUARE_SIZE), LINE_WIDTH)

# Function to draw X or O on the board
def draw_xo(row, col):
    font = pygame.font.Font(None, 120)
    text = font.render(current_player, True, WHITE)
    text_rect = text.get_rect(center=(col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2))
    screen.blit(text, text_rect)

# Function to check for a winner
def check_winner():
    # Check rows
    for row in board:
        if all(cell == current_player for cell in row):
            return True

    # Check columns
    for col in range(GRID_SIZE):
        if all(row[col] == current_player for row in board):
            return True

    # Check diagonals
    if all(board[i][i] == current_player for i in range(GRID_SIZE)) or \
       all(board[i][GRID_SIZE - 1 - i] == current_player for i in range(GRID_SIZE)):
        return True

    return False

# Function to make the bot's move
def make_bot_move():
    empty_cells = [(i, j) for i in range(GRID_SIZE) for j in range(GRID_SIZE) if board[i][j] == '']
    if empty_cells:
        return random.choice(empty_cells)
    else:
        return None

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and current_player == 'X':
            # Get the row and column clicked by the human player
            row = event.pos[1] // SQUARE_SIZE
            col = event.pos[0] // SQUARE_SIZE

            # Check if the cell is empty
            if board[row][col] == '':
                # Update the board
                board[row][col] = current_player

                # Draw X on the board
                draw_xo(row, col)

                # Check for a winner
                if check_winner():
                    print(f"Player {current_player} wins!")
                    pygame.quit()
                    sys.exit()

                # Switch players
                current_player = 'O'

        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and current_player == 'O':
            # Bot's turn
            bot_move = make_bot_move()
            if bot_move:
                row, col = bot_move
                # Update the board
                board[row][col] = current_player

                # Draw O on the board
                draw_xo(row, col)

                # Check for a winner
                if check_winner():
                    print(f"Player {current_player} wins!")
                    pygame.quit()
                    sys.exit()

                # Switch players
                current_player = 'X'

    # Draw the grid
    draw_grid()

    # Update the display
    pygame.display.flip()

    # Set the frames per second
    pygame.time.Clock().tick(30)
