#!/usr/bin/python3
import sys
"""
the n-queen program
"""


def is_safe(board, row, col):
    for i in range(col):
        if board[i] == row or \
           board[i] - i == row - col or \
           board[i] + i == row + col:
            return False
    return True

def solve_nqueens(n):
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = []

    def backtrack(board, col):
        if col == n:
            solutions.append(board[:])
            return
        for row in range(n):
            if is_safe(board, row, col):
                board.append(row)
                backtrack(board, col + 1)
                board.pop()

    backtrack([], 0)

    for solution in solutions:
        formatted_solution = [[i, solution[i]] for i in range(n)]
        print(formatted_solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(n)
