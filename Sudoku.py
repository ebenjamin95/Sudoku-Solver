def sudoku_solver(grid, col, row):
    """
    Solves a given sudoku board and
    returns the solution.
    """
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
    if grid[row][col] > 0:
        return sudoku_solver(grid, col + 1, row)

    for num in range(1, 10):
        if isValid(col, row, grid, num):
            grid[row][col] = num

            if sudoku_solver(grid, col + 1, row):
                return grid

        grid[row][col] = 0

    # If the board is not solvable
    return False


def isValid(col, row, grid, num):
    """
    Checks to make sure the given
    number is valid. Returns True
    or False
    """
    # Check row
    for i in range(len(grid)):
        temp = grid[row][i]
        if temp == num:
            return False

    # Check column
    for i in range(len(grid)):
        temp = grid[i][col]
        if temp == num:
            return False

    # Check 3x3 box
    start_row = row - (row % 3)
    end_row = start_row + 3

    start_col = col - (col % 3)
    end_col = start_col + 3

    for i in range(start_row, end_row):
        for j in range(start_col, end_col):
            if grid[i][j] == num:
                return False

    return True


if __name__ == "__main__":
    board = [[2, 5, 0, 0, 3, 0, 9, 0, 1],
             [0, 1, 0, 0, 0, 4, 0, 0, 0],
             [4, 0, 7, 0, 0, 0, 2, 0, 8],
             [0, 0, 5, 2, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 9, 8, 1, 0, 0],
             [0, 4, 0, 0, 0, 3, 0, 0, 0],
             [0, 0, 0, 3, 6, 0, 0, 7, 2],
             [0, 7, 0, 0, 0, 0, 0, 0, 3],
             [9, 0, 3, 0, 0, 0, 6, 0, 4]]

    # Easy
    board2 = [[0, 0, 4, 5, 0, 0, 2, 8, 0],
              [3, 5, 7, 8, 0, 4, 6, 1, 0],
              [8, 1, 2, 0, 0, 6, 5, 7, 0],
              [0, 4, 0, 3, 8, 0, 7, 0, 0],
              [0, 0, 0, 0, 6, 0, 0, 9, 8],
              [0, 2, 8, 0, 5, 9, 0, 0, 0],
              [0, 6, 0, 0, 0, 0, 8, 3, 0],
              [5, 0, 1, 6, 7, 0, 9, 4, 2],
              [0, 7, 0, 0, 0, 0, 1, 0, 0]]

    # Easy
    board3 = [[0, 3, 0, 0, 0, 0, 9, 0, 6],
              [6, 0, 2, 9, 4, 3, 8, 5, 1],
              [0, 0, 0, 0, 0, 0, 0, 7, 3],
              [3, 9, 1, 7, 0, 0, 0, 6, 8],
              [0, 0, 0, 0, 1, 0, 0, 4, 2],
              [4, 0, 0, 0, 8, 6, 0, 0, 0],
              [9, 4, 7, 0, 3, 0, 0, 0, 0],
              [0, 1, 6, 0, 9, 5, 0, 3, 0],
              [8, 0, 0, 0, 6, 7, 0, 0, 9]]

    # Medium
    board4 = [[0, 0, 0, 0, 0, 4, 0, 0, 2],
              [8, 2, 7, 0, 1, 3, 0, 0, 0],
              [0, 0, 9, 2, 5, 0, 8, 3, 0],
              [0, 0, 0, 8, 0, 0, 0, 5, 0],
              [0, 0, 8, 7, 0, 0, 0, 9, 6],
              [7, 0, 3, 0, 0, 0, 0, 8, 0],
              [1, 0, 0, 4, 0, 9, 0, 6, 0],
              [0, 6, 0, 3, 0, 0, 4, 0, 0],
              [0, 0, 0, 0, 0, 1, 0, 2, 0]]

    board5 = [[0, 5, 1, 0, 9, 2, 4, 0, 8],
              [0, 2, 0, 5, 0, 0, 6, 0, 1],
              [0, 0, 0, 0, 0, 0, 0, 0, 9],
              [0, 1, 7, 0, 0, 8, 0, 6, 4],
              [9, 8, 0, 0, 0, 0, 0, 1, 2],
              [2, 3, 0, 4, 0, 0, 7, 9, 0],
              [4, 0, 0, 0, 0, 0, 0, 0, 0],
              [3, 0, 2, 0, 0, 5, 0, 4, 0],
              [1, 0, 8, 2, 4, 0, 9, 3, 0]]

    ans = sudoku_solver(board, 0, 0)
    sudoku_solver(board, 0, 0)
    for i in range(len(board)):
        print(board[i])

    print()
    print()
    for i in range(len(board2)):
        print(board2[i])
