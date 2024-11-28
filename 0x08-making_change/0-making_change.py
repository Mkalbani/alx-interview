#!/usr/bin/python3
def makeChange(coins, total):
    if total <= 0:
        return 0

    # Create a list to store the minimum'total'
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins are needed to make total 0

    # Fill the dp array
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If the total amount can't be made with the given coins, return -1
    return dp[total] if dp[total] != float('inf') else -1
