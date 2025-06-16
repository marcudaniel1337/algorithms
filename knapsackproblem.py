def knapsack(weights, values, capacity):
    n = len(weights)
    
    # dp[i][w] = max value using first i items with weight limit w
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # option 1: don't take item i-1
            dp[i][w] = dp[i-1][w]
            
            # option 2: take item i-1 if it fits
            if weights[i-1] <= w:
                take_value = dp[i-1][w - weights[i-1]] + values[i-1]
                dp[i][w] = max(dp[i][w], take_value)
    
    return dp[n][capacity]


def knapsack_with_items(weights, values, capacity):
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # fill the table
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i-1][w]  # don't take
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i][w], dp[i-1][w - weights[i-1]] + values[i-1])
    
    # backtrack to find which items we took
    selected = []
    w = capacity
    for i in range(n, 0, -1):
        # if value changed from previous row, we must have taken this item
        if dp[i][w] != dp[i-1][w]:
            selected.append(i-1)  # item index
            w -= weights[i-1]
    
    selected.reverse()  # fix order
    return dp[n][capacity], selected


def knapsack_optimized(weights, values, capacity):
    # only need previous row, save some space
    prev = [0] * (capacity + 1)
    
    for i in range(len(weights)):
        curr = [0] * (capacity + 1)
        for w in range(capacity + 1):
            curr[w] = prev[w]  # don't take item i
            if weights[i] <= w:
                curr[w] = max(curr[w], prev[w - weights[i]] + values[i])
        prev = curr
    
    return prev[capacity]


# test it out
if __name__ == "__main__":
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50
    
    print(f"Max value: {knapsack(weights, values, capacity)}")
    
    max_val, items = knapsack_with_items(weights, values, capacity)
    print(f"Max value: {max_val}")
    print(f"Items taken: {items}")
    
    # show what we actually picked
    total_weight = sum(weights[i] for i in items)
    total_value = sum(values[i] for i in items)
    print(f"Total weight: {total_weight}/{capacity}")
    print(f"Total value: {total_value}")
    
    # bigger test case
    print("\nBigger test:")
    w2 = [1, 3, 4, 5, 7, 9, 10]
    v2 = [1, 4, 5, 7, 8, 9, 10] 
    cap2 = 15
    
    result = knapsack_optimized(w2, v2, cap2)
    print(f"Optimized result: {result}")
