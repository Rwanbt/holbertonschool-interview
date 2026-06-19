#!/usr/bin/python3
import sys


def get_solutions(n):
    """Module to solve the N-Queens problem"""
    solutions = []

    def is_safe(queens, new_col):
        row = len(queens)
        for r, c in enumerate(queens):
            if c == new_col or abs(c - new_col) == abs(r - row):
                return False
        return True

    def backtrack(queens):
        if len(queens) == n:
            print([[r, c] for r, c in enumerate(queens)])
            return

        for col in range(n):
            if is_safe(queens, col):
                backtrack(queens + [col])

    backtrack([])


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    get_solutions(n)


if __name__ == "__main__":
    main()
