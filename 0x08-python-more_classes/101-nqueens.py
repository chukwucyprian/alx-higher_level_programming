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
        if board[i][col] == 1:
            return False

    # Check if there is a queen in the upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check if there is a queen in the upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < len(board):
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens(board, row):
    """
    Recursive function to solve the N Queens problem.

    Args:
        board (list): The current state of the chessboard.
        row (int): The current row index.

    Returns:
        None
    """
    size = len(board)

    if row == size:
        # Print the solution
        for i in range(size):
            print("[" + ", ".join(str(board[i][j]) for j in range(size)) + "]")
        print()
    else:
        for col in range(size):
            if is_safe(board, row, col):
                board[row][col] = 1  # Place the queen

                # Recurse to the next row
                solve_nqueens(board, row + 1)

                board[row][col] = 0  # Backtrack and remove the queen


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

    board = [[0] * n for _ in range(n)]
    solve_nqueens(board, 0)


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
