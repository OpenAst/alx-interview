#!/usr/bin/python3
""" N queens """
import sys


def is_safe(board, row, col, N):
    """ Check if it is safe to place a queen at a particular position """
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False


    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True


def solveNQueensUtil(board, row, N, solutions):
    """ Utility function for N-Queens puzzle """
    if row >= N:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return 

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solveNQueensUtil(board, row + 1, N, solutions)
            board[row][col] = 0

    return False


def solveNQueens(N):
    """ Solves the NQueen puzzle """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    
    try:
        N = int(N)
    except ValueError:
        print("N must be a number")
        exit(1)
    if N < 4:
        print("N must be at least 4")
        exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]

    solutions = []

    solveNQueensUtil(board, 0, N, solutions)

    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    N = sys.argv[1]
    solveNQueens(N)
