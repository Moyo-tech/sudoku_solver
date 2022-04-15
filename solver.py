class Solver:
    def __init__(self):
        self.no_rows_col = 9  # No of rows and cols that is required
        self.count = 0

    '''
    is_valid() functin: Determines if on a certain position we can put
    a number returns true if it is possible to put a number and returns 
    an error otherwise. Checks row then checks the columns then checks the grid 
    '''

    def is_valid(self, sudoku, row, col, num):
        # Checking if the same number exists in same row
        for i in range(9):
            if sudoku[row][i] == num:
                return

        # Checking if the same number exists in the same column, returning an error from
        # gui.py  if it does
        for i in range(9):
            if sudoku[i][col] == num:
                return

    # Checking if the same number exists in the particular 3 by 3 grid
        start_row = row - row % 3
        start_col = col - col % 3
        for i in range(3):
            for j in range(3):
                if sudoku[start_row + i][start_col + j] == num:
                    return

        return True  # This would get executed if none of the above condition are satisfied

    '''Main Algorithm to solve the Sudoku '''

    def solve_sudoku(self, sudoku, row, col):
        self.count += 1

        if self.count > 1000:
            return False

        # Base condition: This means we are at the end of the board and so the sudoku is solved
        if row == self.no_rows_col - 1 and col == self.no_rows_col:
            return True

    # Moving to the next row when last column is reached
        if col == self.no_rows_col:
            row += 1
            col = 0

    # Checking if the number is assigned to current position, if
    # there is a number in a position in our puzzle
        if sudoku[row][col] > 0:
            # We test out the next column
            return self.solve_sudoku(sudoku, row, col + 1)

        # Trying each number from 1 to 9
        for num in range(1, self.no_rows_col + 1):
            # Checking if it is okay to assign a particular number
            if self.is_valid(sudoku, row, col, num):
                sudoku[row][col] = num  # Assigning the number in the sudoku

                # If the number assigned is correct we would also check for
                # possibilities with next column
                if self.solve_sudoku(sudoku, row, col + 1):
                    return True

            # If our assumption was wrong we would backtrack(go back one step)
            # and try to check for another number in the previous postion
            sudoku[row][col] = 0  # Backtracking

        return False

    # Function to return the solved sudoku if it is solvable
    def main_solver(self, sudoku):
        result = self.solve_sudoku(sudoku, 0, 0)

        # If condition to check if sudoku is solvable starting from 0th row and 0th column
        if result:
            self.count = 0
            return sudoku
        else:
            self.count = 0
            return "no"
