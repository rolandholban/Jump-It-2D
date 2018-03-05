#!/usr/bin/env python3

import sys

def jumpIt2D(matrix, rows, columns):
    # Cost table
    costs = []
    for row in range(rows):
        costs.append([0] * columns)

    # Temporary variable for indexing purposes
    tRow = rows - 1
    tCol = columns - 1

    # Fill in default cells
    costs[tRow][tCol] = matrix[tRow][tCol]
    costs[tRow-1][tCol] = matrix[tRow-1][tCol] + costs[tRow][tCol]
    costs[tRow][tCol-1] = matrix[tRow][tCol-1] + costs[tRow][tCol]
    costs[tRow-1][tCol-1] = matrix[tRow-1][tCol-1] + min(costs[tRow-1][tCol], costs[tRow][tCol-1])

    # Fill in bottom row
    for col in range(tCol-2,-1,-1):
        costs[tRow][col] = matrix[tRow][col] + min(costs[tRow][col+1], costs[tRow][col+2])

    # Fill in rightmost column
    for row in range(tRow-2,-1,-1):
        costs[row][tCol] = matrix[row][tCol] + min(costs[row+1][tCol], costs[row+2][tCol])

    # Fill in second to last row
    for col in range(tCol-2,-1,-1):
        costs[tRow-1][col] = matrix[tRow-1][col] + min(costs[tRow-1][col+1], costs[tRow-1][col+2], costs[tRow][col])

    # Fill in second to right most column
    for row in range(tRow-2,-1,-1):
        costs[row][tCol-1] = matrix[row][tCol-1] + min(costs[row+1][tCol-1], costs[row+2][tCol-1], costs[row][tCol])

    # Fill in the rest
    for row in range(tRow-2,-1,-1):
        for col in range(tCol-2,-1,-1):
            costs[row][col] = matrix[row][col] + min(costs[row+1][col], costs[row+2][col], costs[row][col+1], costs[row][col+2])  

    print(costs[0][0])


def main():
    # Read the input file into a matrix
    with open(sys.argv[1], 'r') as f:
        x = f.readlines()
        rows = int(x[0].split()[0])
        columns = int(x[0].split()[1])
        matrix = [list(map(int, x[i].split())) for i in range(1, len(x))]

    # Calculate optimal cost for traversing the matrix
    jumpIt2D(matrix, rows, columns)

main()
