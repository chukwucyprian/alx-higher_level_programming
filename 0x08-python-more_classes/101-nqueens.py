#!/usr/bin/python3

import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at a given position.

    Args:
        board (list): The current state of the chessboard.
        row (int): The row index to check.
        col (int): The column index to check.

    Returns:
        bool: True if it's safe to place a queen, False otherwise.
    """
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col:
            return False

    # Check if there is a queen in the upper-left diagonal
    for i, j in enumerate(board[:row]):
        if j == col - (row - i):
            return False

    # Check if there is a queen in the upper-right diagonal
    for i, j in enumerate(board[:row]):
        if j == col + (row - i):
            return False

    return True


def solve_nqueens(board, row, n):
    """
    Recursive function to solve the N Queens problem.

    Args:
        board (list): The current state of the chessboard.
        row (int): The current row index.
        n (int): The size of the chessboard.

    Returns:
        None
    """
    if row == n:
        # Print the solution
        solution = [[i, board[i]] for i in range(n)]
        print(solution)
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col  # Place the queen
            solve_nqueens(board, row + 1, n)
            board[row] = -1  # Backtrack and remove the queen


def nqueens(n):
    """
    Solve the N Queens problem for a given board size.

    Args:
        n (int): The size of the chessboard and the number of queens.

    Returns:
        None
    """
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solve_nqueens(board, 0, n)


# Check if the program is called with the correct number of arguments
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

# Get the value of N from the command line argument
try:
    N = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)

# Solve the N Queens problem
nqueens(N)
