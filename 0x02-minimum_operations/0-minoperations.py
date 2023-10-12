#!/usr/bin/python3
"""
defininig the minOperations
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n H characters in the file.

    Args:
      n: The number of H characters desired.

    Returns:
      The fewest number of operations needed, or 0 if n is impossible to achieve.
    """
    if n <= 1:
        return n

    min_operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            n //= divisor
            min_operations += divisor

        divisor += 1

    return min_operations


