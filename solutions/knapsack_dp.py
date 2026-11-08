def knapsack_dp(items, capacity):
    dp = [0] * (capacity + 1)
    
    for weight, val in items:
        for c in range(capacity, weight - 1, -1):
            dp[c] = max(dp[c], dp[c - weight] + val)
            
    return dp[capacity]
