def matrix_chain_order(p):
    n = len(p) - 1  # number of matrices
    
    # dp[i][j] = min cost to multiply matrices from i to j
    dp = [[0 for _ in range(n)] for _ in range(n)]
    
    # l is chain length
    for l in range(2, n + 1):  # start from length 2
        for i in range(n - l + 1):
            j = i + l - 1
            dp[i][j] = float('inf')
            
            # try all possible splits between i and j
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + p[i] * p[k+1] * p[j+1]
                dp[i][j] = min(dp[i][j], cost)
    
    return dp[0][n-1]


def matrix_chain_with_order(p):
    n = len(p) - 1
    dp = [[0 for _ in range(n)] for _ in range(n)]
    split = [[0 for _ in range(n)] for _ in range(n)]  # track where we split
    
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            dp[i][j] = float('inf')
            
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + p[i] * p[k+1] * p[j+1]
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    split[i][j] = k  # remember this split point
    
    return dp[0][n-1], split


def print_optimal_parens(split, i, j):
    # recursively build the parenthesization string
    if i == j:
        return f"M{i}"
    else:
        k = split[i][j]
        left = print_optimal_parens(split, i, k)
        right = print_optimal_parens(split, k+1, j)
        return f"({left} * {right})"


def matrix_chain_recursive(p, i, j, memo=None):
    # recursive version with memoization (just for comparison)
    if memo is None:
        memo = {}
    
    if i == j:
        return 0
    
    if (i, j) in memo:
        return memo[(i, j)]
    
    min_cost = float('inf')
    for k in range(i, j):
        cost = (matrix_chain_recursive(p, i, k, memo) + 
                matrix_chain_recursive(p, k+1, j, memo) + 
                p[i] * p[k+1] * p[j+1])
        min_cost = min(min_cost, cost)
    
    memo[(i, j)] = min_cost
    return min_cost


# test cases
if __name__ == "__main__":
    # matrices: A1(1x2), A2(2x3), A3(3x4), A4(4x5)
    # p = [1, 2, 3, 4, 5] represents dimensions
    p1 = [1, 2, 3, 4, 5]
    print(f"Min multiplications: {matrix_chain_order(p1)}")
    
    cost, splits = matrix_chain_with_order(p1)
    print(f"Cost: {cost}")
    print(f"Optimal order: {print_optimal_parens(splits, 0, len(p1)-2)}")
    
    # bigger example
    print("\nBigger example:")
    p2 = [40, 20, 30, 10, 30]  # A1(40x20), A2(20x30), A3(30x10), A4(10x30)
    cost2, splits2 = matrix_chain_with_order(p2)
    print(f"Cost: {cost2}")
    print(f"Order: {print_optimal_parens(splits2, 0, len(p2)-2)}")
    
    # compare with recursive
    print(f"Recursive result: {matrix_chain_recursive(p2, 0, len(p2)-2)}")
    
    # show what the dimensions mean
    print("\nMatrix dimensions:")
    for i in range(len(p2)-1):
        print(f"M{i}: {p2[i]} x {p2[i+1]}")
