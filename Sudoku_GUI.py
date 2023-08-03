import pygame
from Sudoku import isValid, sudoku_solver
from constants import *

pygame.font.init()


class Board:
    board = [[0, 5, 1, 0, 9, 2, 4, 0, 8],
              [0, 2, 0, 5, 0, 0, 6, 0, 1],
              [0, 0, 0, 0, 0, 0, 0, 0, 9],
              [0, 1, 7, 0, 0, 8, 0, 6, 4],
              [9, 8, 0, 0, 0, 0, 0, 1, 2],
              [2, 3, 0, 4, 0, 0, 7, 9, 0],
              [4, 0, 0, 0, 0, 0, 0, 0, 0],
              [3, 0, 2, 0, 0, 5, 0, 4, 0],
              [1, 0, 8, 2, 4, 0, 9, 3, 0]]

    def __init__(self, rows, cols, width, height):
        self.rows = rows
        self.cols = cols
        self.width = width
        self.height = height
        self.squares = [[Square(self.board[i][j], i, j, width, height) for j in range(cols)]
                        for i in range(rows)]
        self.selected = None
        self.solved_board = sudoku_solver(self.board, 0, 0)

    def solve(self, window):
        """
        Solves game when
        space bar is pressed.
        """
        grid = self.squares
        row = 0
        col = 0
        return self.solve_helper(grid, col, row, window)

    def solve_helper(self, grid, col, row, window):
        # Once the last cell is filled,
        # the program ends
        if row == 8 and col == 9:
            return True

        # Checks if the current column is out
        # of range. If so, reset col and move
        # to next row
        if col > 8:
            row += 1
            col = 0

        # Checks if there is already a number
        # given
        if grid[row][col].get_value() > 0:
            return self.solve_helper(grid, col + 1, row, window)

        for num in range(1, 10):
            if self.isValid(col, row, grid, num):
                # grid[row][col] = num
                grid[row][col].set_value(num)
                grid[row][col].draw(window)
                pygame.display.update()

                if self.solve_helper(grid, col + 1, row, window):
                    return grid

            # grid[row][col] = 0
            grid[row][col].clear()
            grid[row][col].draw(window)
            pygame.display.update()

        # If the board is not solvable
        return False

    def isValid(self, col, row, grid, num):
        """
        Checks to make sure the given
        number is valid. Returns True
        or False
        """
        # Check row
        for i in range(len(grid)):
            temp = grid[row][i].get_value()
            if temp == num:
                return False

        # Check column
        for i in range(len(grid)):
            temp = grid[i][col].get_value()
            if temp == num:
                return False

        # Check 3x3 box
        start_row = row - (row % 3)
        end_row = start_row + 3

        start_col = col - (col % 3)
        end_col = start_col + 3

        for i in range(start_row, end_row):
            for j in range(start_col, end_col):
                if grid[i][j].get_value() == num:
                    return False

        return True

    def draw(self, window):

        # Fills screen with a certain color
        window.fill(WHITE)
        row_height = HEIGHT // ROWS
        col_width = WIDTH // COLS

        # Creates the light squares of the sudoku board
        # Sets up the Original Values
        for row in range(ROWS):
            for col in range(COLS):
                pygame.draw.rect(window, GRAY, (col * col_width, row * row_height, col_width, row_height), 1)
                self.squares[row][col].draw(window)
                if self.squares[row][col].get_value() != 0:
                    pygame.draw.rect(window, BLUE, (col * col_width, row * row_height, col_width, row_height), 1)

        # Dark grid lines
        pygame.draw.line(window, BLACK, (col_width * 3, 0), (col_width * 3, HEIGHT), 3)
        pygame.draw.line(window, BLACK, (col_width * 6, 0), (col_width * 6, HEIGHT), 3)

        pygame.draw.line(window, BLACK, (0, row_height * 3), (WIDTH, row_height * 3), 3)
        pygame.draw.line(window, BLACK, (0, row_height * 6), (WIDTH, row_height * 6), 3)

        # Draw original squares and values
        # for i in range(ROWS):
        #     for j in range(COLS):
        #         self.squares[i][j].draw(window)
        #         pygame.draw.rect(window, GREEN, (space_x, space_y, col_width, row_height), 1)

        pygame.display.update()

    def place(self, val, window):
        """
        Places a value on
        the board after the
        user hits Enter.
        """
        space = self.width / 9
        x, y = self.selected
        row = int(y // space)
        col = int(x // space)

        # Make black if correct
        if self.solved_board[row][col] == val:
            self.squares[row][col].set_value(val)
            self.squares[row][col].draw(window)

        # Display red x if incorrect
        else:
            red_x_image = pygame.image.load('red-x.png')
            red_x = pygame.transform.scale(red_x_image, (space, space))
            space_x = space * col
            space_y = space * row

            img_width = red_x.get_width() // 2
            img_height = red_x.get_height() // 2

            new_x = space_x + ((space // 2) - img_width)
            new_y = space_y + ((space // 2) - img_height)

            window.blit(red_x, (new_x, new_y))
            pygame.display.flip()

    def trial(self, val, x_coord, y_coord, window):
        """
        Creates a number on the board
        that the user can try to see
        if it would work.
        """

        space = self.width / 9
        row = int(y_coord // space)
        col = int(x_coord // space)

        self.squares[row][col].set_temp(val)
        self.squares[row][col].draw(window)

    # def click(self, x_coord, y_coord):
    #     """
    #     Returns the position of
    #     the mouse when it's clicked.
    #     """
    #     return int(x_coord), int(y_coord)

    def select(self, x_coord, y_coord):
        """
        Determines which square has
        been selected/clicked on.
        """
        space = self.width / 9
        row = int(y_coord // space)
        col = int(x_coord // space)

        # Resets all other squares so only
        # one is highlighted
        for i in range(ROWS):
            for j in range(COLS):
                self.squares[i][j].selected = False

        self.squares[row][col].selected = True


class Square:
    rows = 9
    cols = 9

    def __init__(self, val, row, col, width, height):
        self.val = val
        self.temp = 0
        self.row = row
        self.col = col
        self.width = width
        self.height = height
        self.selected = False
        self.isOriginal = False

    def draw(self, window):
        # Space between each row and column
        sq_width = self.width / 9
        sq_height = self.height / 9

        # Exact location of the start
        # of each row and column on screen
        space_x = sq_width * self.col
        space_y = sq_height * self.row

        # Setting for font
        fnt = pygame.font.SysFont("calibri", 38)

        # Sets the permanent value
        if self.val != 0:
            text = fnt.render(str(self.val), False, BLACK)
            num_width = text.get_width() // 2
            num_height = text.get_height() // 2
            x = space_x + ((sq_width // 2) - num_width)
            y = space_y + ((sq_height // 2) - num_height)
            image = pygame.Surface((num_width * 2, num_height * 2))
            image.fill(WHITE)
            window.blit(image, (x, y))
            window.blit(text, (x, y))

        # Sets the trial value
        if self.temp != 0 and self.val == 0:
            text = fnt.render(str(self.temp), False, GRAY)
            num_width = text.get_width() // 2
            num_height = text.get_height() // 2
            x = space_x + ((sq_width // 2) - num_width)
            y = space_y + ((sq_height // 2) - num_height)
            window.blit(text, (x, y))

        # Highlight square if clicked on
        if self.selected:
            pygame.draw.rect(window, RED, (space_x, space_y, sq_width, sq_height), 1)

    def set_value(self, val):
        """
        Sets the permanent value
        in the square.
        """
        self.val = val

    def get_value(self):
        """
        Returns the current
        value of the square.
        """
        return self.val

    def set_temp(self, val):
        """
        Sets the temporary value
        in the square.
        """
        self.temp = val

    def clear(self):
        """
        Clears the current
        square.
        """
        self.set_value(0)
        self.set_temp(0)


def main():
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    board = Board(ROWS, COLS, WIDTH, HEIGHT)
    clock = pygame.time.Clock()
    key = 0
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
                pos = pygame.mouse.get_pos()
                print(pos)
                # x, y = board.click(pos[0], pos[1])
                board.select(pos[0], pos[1])
                board.selected = (pos[0], pos[1])

            # Check: did any of the following
            # keys get entered/pressed?
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9

                # Enters number after trial
                if event.key == pygame.K_RETURN:
                    x, y = board.selected
                    space = board.width / 9
                    i = int(y // space)
                    j = int(x // space)
                    square = board.squares[i][j]
                    if square.temp != 0:
                        board.place(square.temp, SCREEN)

            # Check: Space bar pressed (solve game)?
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    board.solve(SCREEN)

        # Sketches trial value
        if board.selected and key != 0:
            board.trial(key, board.selected[0], board.selected[1], SCREEN)
            key = 0

        board.draw(SCREEN)

    pygame.quit()


if __name__ == "__main__":
    main()
