import pygame
from tictactoegame import TicTacToeGame
from ttt_minimax import MinimaxAlgorithm

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600

# Initialize game and screen
game = TicTacToeGame(grid_size=TicTacToeGame.GRID_SIZE)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Main game loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not game.is_game_over():
            # Handle mouse clicks for human player (X) moves
            x, y = event.pos
            position = (x // (WIDTH // game.get_grid_size())) + (y // (HEIGHT // game.get_grid_size())) * game.get_grid_size()
            game.make_move(position)
    keys = pygame.key.get_pressed()
    if not game.is_game_over() and keys[pygame.K_SPACE]:
        # Make a move for the bot player (O) using the minimax algorithm
        if game.current_player == 'O':
            algorithm = MinimaxAlgorithm('O')
            position = algorithm.make_move(game)
            game.make_move(position)

    # Draw the board
    screen.fill((0, 0, 0))
    cell_size = WIDTH // game.get_grid_size()
    for i in range(1, game.get_grid_size()):
        pygame.draw.line(screen, (255, 255, 255), (i * cell_size, 0), (i * cell_size, HEIGHT), 2)
        pygame.draw.line(screen, (255, 255, 255), (0, i * cell_size), (WIDTH, i * cell_size), 2)

    # Draw X and O
    font = pygame.font.Font(None, cell_size)
    for row in range(game.get_grid_size()):
        for col in range(game.get_grid_size()):
            index = row * game.get_grid_size() + col
            if game.get_board()[index] == 'X':
                text = font.render('X', True, (255, 255, 255))
                screen.blit(text, (col * cell_size + cell_size // 4, row * cell_size + cell_size // 4))
            elif game.get_board()[index] == 'O':
                text = font.render('O', True, (255, 255, 255))
                screen.blit(text, (col * cell_size + cell_size // 4, row * cell_size + cell_size // 4))

    # Update the display
    pygame.display.flip()

    # Check for game over
    if game.is_game_over():
        running = False

# Quit Pygame
pygame.quit()
