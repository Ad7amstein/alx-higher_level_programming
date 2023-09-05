#!/usr/bin/python3
"""Defines an nqueens and solve function."""
import sys


solutions = []


def solve(N, grid, ans=[], r=0, c=0, NQueens=0):
    """Function solver to find all possible solutions for N-Queens problem.

    Args:
        N (int): Grid size.
        grid ([[]]): The chess board.
        ans ([[]]): To store the current solution found.
        r (int): Represents the row number.
        c (int): Represents the column number.
        NQueens (int): The queens places yet.
    """
    if NQueens == N:
        solutions.append(ans[:])
        return
    if r >= N or c >= N or r < 0 or c < 0:
        return

    for i in range(N):
        if isValid(grid, r, i, N):
            NQueens += 1
            grid[r][i] = 1
            ans.append([r, i])
            solve(N, grid, ans, r + 1, i, NQueens)
            grid[r][i] = 0
            ans.pop()
            NQueens -= 1


def isValid(grid, i, j, N):
    """Checks if the current position is valid to place a queen.

    Args:
        grid ([[]]): The chess board.
        i (int): Represents the row number.
        j (int): Represents the column number.N (int): Grid size.
        N (int): Grid size.

    Returns:
        True: If the current position is valid
        False: If the current position is invalid
    """
    # Check row
    if not all(grid[i][x] == 0 for x in range(N)):
        return False

    # Check column
    if not all(grid[x][j] == 0 for x in range(N)):
        return False

    # Check d1
    x, y = i, j
    while x >= 0 and y >= 0:
        if grid[x][y]:
            return False
        x -= 1
        y -= 1

    x, y = i, j
    while x < N and y < N:
        if grid[x][y]:
            return False
        x += 1
        y += 1

    # Check d2
    x, y = i, j
    while x < N and y >= 0:
        if grid[x][y]:
            return False
        x += 1
        y -= 1

    x, y = i, j
    while x >= 0 and y < N:
        if grid[x][y]:
            return False
        x -= 1
        y += 1

    return True


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    grid = [[0 for _ in range(N)] for _ in range(N)]
    solve(N, grid)
    for solution in solutions:
        print(solution)
