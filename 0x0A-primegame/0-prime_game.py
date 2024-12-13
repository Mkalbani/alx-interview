#!/usr/bin/python3
"""
Prime Game: Determine the winner of a game where players pick primes optimally.
"""


def isWinner(x, nums):
    """
    Determines the winner of the game after x rounds.

    Args:
        x (int): Number of rounds.
        nums (list): List of integers representing the range of numbers.

    Returns:
        str or None: The name of the player
        with the most wins ("Maria" or "Ben"),
                     or None if there's no winner.
    """
    if not nums or x <= 0:
        return None

    max_num = max(nums)
    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(max_num ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_num + 1, i):
                sieve[j] = False

    primes_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        primes_count[i] = primes_count[i - 1] + (1 if sieve[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if primes_count[n] % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
