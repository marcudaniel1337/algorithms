def add_matrix(A, B):
    """Add two matrices element-wise."""
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]

def sub_matrix(A, B):
    """Subtract matrix B from matrix A element-wise."""
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]

def split_matrix(M):
    """
    Split given matrix M into four sub-matrices (quarters).
    M is assumed to be n x n where n is even.
    """
    n = len(M)
    mid = n // 2
    A11 = [row[:mid] for row in M[:mid]]
    A12 = [row[mid:] for row in M[:mid]]
    A21 = [row[:mid] for row in M[mid:]]
    A22 = [row[mid:] for row in M[mid:]]
    return A11, A12, A21, A22

def strassen(A, B):
    """
    Multiply two square matrices A and B using Strassen's algorithm.

    Args:
        A, B: square matrices (lists of lists) of size n x n,
              where n is a power of 2 for simplicity.

    Returns:
        Product matrix of size n x n.
    """
    n = len(A)

    # Base case: 1x1 matrix multiplication
    if n == 1:
        return [[A[0][0] * B[0][0]]]

    # Split matrices into quarters
    A11, A12, A21, A22 = split_matrix(A)
    B11, B12, B21, B22 = split_matrix(B)

    # Compute the 7 products (recursive calls)
    # Using Strassen's formulas:
    M1 = strassen(add_matrix(A11, A22), add_matrix(B11, B22))  # (A11 + A22) * (B11 + B22)
    M2 = strassen(add_matrix(A21, A22), B11)                   # (A21 + A22) * B11
    M3 = strassen(A11, sub_matrix(B12, B22))                   # A11 * (B12 - B22)
    M4 = strassen(A22, sub_matrix(B21, B11))                   # A22 * (B21 - B11)
    M5 = strassen(add_matrix(A11, A12), B22)                   # (A11 + A12) * B22
    M6 = strassen(sub_matrix(A21, A11), add_matrix(B11, B12))  # (A21 - A11) * (B11 + B12)
    M7 = strassen(sub_matrix(A12, A22), add_matrix(B21, B22))  # (A12 - A22) * (B21 + B22)

    # Calculate the resulting quarters of the product matrix C
    C11 = add_matrix(sub_matrix(add_matrix(M1, M4), M5), M7)  # M1 + M4 - M5 + M7
    C12 = add_matrix(M3, M5)                                  # M3 + M5
    C21 = add_matrix(M2, M4)                                  # M2 + M4
    C22 = add_matrix(sub_matrix(add_matrix(M1, M3), M2), M6)  # M1 + M3 - M2 + M6

    # Combine quarters into a full matrix
    new_matrix = []
    for i in range(n // 2):
        new_matrix.append(C11[i] + C12[i])
    for i in range(n // 2):
        new_matrix.append(C21[i] + C22[i])

    return new_matrix

def print_matrix(M):
    """Helper function to nicely print a matrix."""
    for row in M:
        print(' '.join(map(str, row)))
    print()

if __name__ == "__main__":
    # Example usage:
    A = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 8, 7, 6],
        [5, 4, 3, 2]
    ]

    B = [
        [1, 0, 2, 1],
        [0, 1, 0, 2],
        [1, 0, 1, 0],
        [0, 2, 1, 1]
    ]

    print("Matrix A:")
    print_matrix(A)
    print("Matrix B:")
    print_matrix(B)

    C = strassen(A, B)

    print("Product Matrix C = A * B:")
    print_matrix(C)
