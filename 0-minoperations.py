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

  # If n is 1, then we only need to copy and paste the initial H character.
  if n == 1:
    return 1

  # If n is even, then we can copy and paste the first n / 2 H characters to get n H characters.
  if n % 2 == 0:
    return 2 + minOperations(n // 2)

  # If n is odd, then we need to copy and paste the first (n - 1) / 2 H characters, and then copy and paste the entire file.
  return 3 + minOperations((n - 1) // 2)


