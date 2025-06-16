def solve_sudoku(board):
    """
    Solve the Sudoku puzzle using backtracking.
    The board is a 9x9 list of lists, with empty cells represented by 0.
    Modifies the board in place and returns True if solved, False otherwise.
    """

    def find_empty():
        """
        Find an empty cell (represented by 0) in the board.
        Returns a tuple (row, col) if found, or None if no empty cells.
        """
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return i, j  # row, col of empty cell
        return None

    def is_valid(num, pos):
        """
        Check if placing 'num' in position 'pos' (row, col) is valid.
        Valid means:
        - 'num' does not already appear in the same row.
        - 'num' does not already appear in the same column.
        - 'num' does not already appear in the 3x3 sub-box.
        """

        row, col = pos

        # Check row
        for j in range(9):
            if board[row][j] == num and j != col:
                return False

        # Check column
        for i in range(9):
            if board[i][col] == num and i != row:
                return False

        # Check 3x3 box
        box_start_row = (row // 3) * 3
        box_start_col = (col // 3) * 3

        for i in range(box_start_row, box_start_row + 3):
            for j in range(box_start_col, box_start_col + 3):
                if board[i][j] == num and (i, j) != pos:
                    return False

        # Passed all checks, valid placement
        return True

    def backtrack():
        """
        Main backtracking function:
        - Find an empty cell.
        - If none found, puzzle is solved.
        - Otherwise, try placing numbers 1-9 in that cell.
        - If a number is valid, place it and recurse.
        - If recursion fails, backtrack and try next number.
        """
        empty = find_empty()

        # No empty cell means puzzle solved
        if not empty:
            return True

        row, col = empty

        for num in range(1, 10):  # Try numbers 1 through 9
            if is_valid(num, (row, col)):
                board[row][col] = num  # Tentatively place number

                if backtrack():  # Recurse
                    return True

                board[row][col] = 0  # Backtrack, remove number

        # If no valid number found, trigger backtracking
        return False

    return backtrack()


def print_board(board):
    """
    Helper function to nicely print the Sudoku board.
    Adds lines to separate 3x3 boxes.
    """
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)  # Separator line

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("| ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


if __name__ == "__main__":
    # Example Sudoku puzzle (0 means empty)
    sudoku_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9],
    ]

    print("Original Sudoku board:\n")
    print_board(sudoku_board)

    if solve_sudoku(sudoku_board):
        print("\nSolved Sudoku board:\n")
        print_board(sudoku_board)
    else:
        print("No solution exists for the given Sudoku puzzle.")
