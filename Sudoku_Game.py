# Import pygame
import pygame
from constants import *


# Initialize the pygame library
pygame.init()

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# Window Title
pygame.display.set_caption(TITLE)

# Frames per second
# Keeps game running the same speed regardless of computer
FPS = 60


class Board:
    def __init__(self):
        self._board = [[]]

    def draw_screen(self, window):
        # Fills screen with a certain color
        SCREEN.fill(WHITE)
        row_height = HEIGHT//ROWS
        col_width = WIDTH//COLS

        # Creates the light squares of the sudoku board
        for row in range(ROWS):
            for col in range(COLS):
                pygame.draw.rect(window, GRAY, (col*col_width, row*row_height, col_width, row_height), 1)

        # Dark grid lines
        pygame.draw.line(window, BLACK, (col_width*3, 0), (col_width*3, HEIGHT), 2)
        pygame.draw.line(window, BLACK, (col_width*6, 0), (col_width*6, HEIGHT), 2)

        pygame.draw.line(window, BLACK, (0, row_height*3), (WIDTH, row_height*3), 2)
        pygame.draw.line(window, BLACK, (0, row_height*6), (WIDTH, row_height*6), 2)

        pygame.display.update()


def solve_game():
    """
    Solves the sudoku game
    after space bar is pressed
    :return:
    """



# Where game loop will be located
def main():
    board = Board()
    clock = pygame.time.Clock()
    # Game loop prevents game from opening and
    # then instantly closing
    running = True
    while running:

        # Checks for the different events
        # occurring in pygame
        clock.tick(FPS)
        for event in pygame.event.get():

            # Check: did user quit window?
            if event.type == pygame.QUIT:
                running = False

            # Check: mouse clicked on screen?
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass

            # Check: Space bar pressed (solve game)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    solve_game()

        board.draw_screen(SCREEN)

    pygame.quit()


if __name__ == "__main__":
    main()
