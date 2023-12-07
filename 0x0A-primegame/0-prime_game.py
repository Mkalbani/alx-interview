#!/usr/bin/python3
"""
Defining the prime game
"""


def isWinner(x, nums):
    def sieve_of_eratosthenes(n):
        """
        constricting the varibales
        """
        primes = [True] * (n + 1)
        primes[0], primes[1] = False, False

        p = 2
        while p * p <= n:
            if primes[p]:
                for i in range(p * p, n + 1, p):
                    primes[i] = False
            p += 1

        return [i for i in range(n + 1) if primes[i]]

    def calculate_winner(n):
        """
        defines the winner function
        """
        primes = sieve_of_eratosthenes(n)
        if n in primes:
            return "Maria"  # Maria wins if the given number itself is prime

        for prime in primes:
            if n % prime == 0:
                return "Ben"  # Ben wins if any prime factor is present

        return "Maria"  # Maria wins if no prime factor found


    maria_wins = 0
    ben_wins = 0

    for i in range(x):
        winner = calculate_winner(nums[i])
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Ben"
    elif ben_wins > maria_wins:
        return "Maria"
    else:
        return None
