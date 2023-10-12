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
    # Assign a value to the variable minOperations.
  # Assign a value to the variable min_operations.
  if n < 2:
      return n
  min_operations = 2
  operations = 2
  x = 2

  while x < n:
      if n % x == 0:
          min_operations += 1
          operations = x
      x += operations
      min_operations += 1

  return min_operations
