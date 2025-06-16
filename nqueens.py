def solve_n_queens(n):
    """
    Solve the N-Queens problem for a board of size n x n.
    Return all distinct solutions where n queens are placed on the board
    so that no two queens threaten each other.

    Each solution is represented as a list of strings,
    where 'Q' indicates a queen and '.' an empty space.
    """

    # This will hold all the valid board configurations we find
    solutions = []

    # Initialize an empty chessboard represented as a 2D list.
    # Each position starts with '.', meaning no queen placed yet.
    board = [['.' for _ in range(n)] for _ in range(n)]

    def is_safe(row, col):
        """
        Check if placing a queen at (row, col) is safe.
        It is safe if no other queen can attack this position.

        We only need to check:
        - The same column in previous rows
        - The upper-left diagonal
        - The upper-right diagonal

        Because we place queens row by row from top to bottom,
        we don't need to check rows below the current row.
        """

        # Check the same column upwards
        for r in range(row):
            if board[r][col] == 'Q':
                # Found a queen in the same column
                return False

        # Check upper-left diagonal
        r, c = row - 1, col - 1
        while r >= 0 and c >= 0:
            if board[r][c] == 'Q':
                # Found a queen on the upper-left diagonal
                return False
            r -= 1
            c -= 1

        # Check upper-right diagonal
        r, c = row - 1, col + 1
        while r >= 0 and c < n:
            if board[r][c] == 'Q':
                # Found a queen on the upper-right diagonal
                return False
            r -= 1
            c += 1

        # If no conflicts, it’s safe to place the queen here
        return True

    def backtrack(row=0):
        """
        Try placing queens starting from the given row.
        This function uses recursion and backtracking:
        - If we manage to place queens on all rows, save the solution.
        - Otherwise, try each column in the current row and recurse.
        """

        # Base case: If we've reached the end, record the solution
        if row == n:
            # Convert each row from list of chars to string and save
            solution = [''.join(r) for r in board]
            solutions.append(solution)
            return

        # Try placing a queen in every column for the current row
        for col in range(n):
            if is_safe(row, col):
                # Place the queen
                board[row][col] = 'Q'
                # Recurse to next row to place next queen
                backtrack(row + 1)
                # Backtrack: remove the queen and try another column
                board[row][col] = '.'

    # Start the process from the first row
    backtrack()

    # After exploring all possibilities, return all found solutions
    return solutions


if __name__ == "__main__":
    # Choose the size of the chessboard (e.g., 4x4)
    n = 4
    print(f"Solving {n}-Queens Problem...\n")

    # Get all valid board configurations
    all_solutions = solve_n_queens(n)

    print(f"Total solutions found: {len(all_solutions)}\n")

    # Print all the solutions in a readable format
    for index, solution in enumerate(all_solutions, start=1):
        print(f"Solution #{index}:")
        for row in solution:
            print(row)
        print()  # Empty line between solutions
