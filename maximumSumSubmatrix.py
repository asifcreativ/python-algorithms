matrix = [
    [5, 3, -1, 5],
    [-7, 3, 7, 4],
    [12, 8, 0, 0],
    [1, -8, -8, 2]
]
size = 2


# time: O(wh) | space: O(wh)
def maximumSumSubmatrix(matrix, size):
    sums = [[0 for col in row] for row in matrix]
    fillMatrixWithSums(sums, matrix)
    runningMaxSum = float("-inf")

    for row in range(size - 1, len(sums)):
        for col in range(size - 1, len(sums[row])):
            total = sums[row][col]

            touchTopBorder = row - size < 0
            touchLeftBorder = col - size < 0

            if not touchTopBorder:
                total -= sums[row - size][col]

            if not touchLeftBorder:
                total -= sums[row][col - size]

            if not touchTopBorder and not touchLeftBorder:
                total += sums[row - size][col - size]

            runningMaxSum = max(runningMaxSum, total)
    return runningMaxSum


def fillMatrixWithSums(sums, matrix):
    sums[0][0] = matrix[0][0]

    # fill first row
    for col in range(1, len(sums[0])):
        sums[0][col] = sums[0][col - 1] + matrix[0][col]

    # fill first column
    for row in range(1, len(sums)):
        sums[row][0] = sums[row - 1][0] + matrix[row][0]

    # fill rest of the sums matrix
    # FORMULA: current + up + left - diagonalTopLeft
    for row in range(1, len(sums)):
        for col in range(1, len(sums[row])):
            value = matrix[row][col]
            up = sums[row - 1][col]
            left = sums[row][col - 1]
            diagonalTopLeft = sums[row - 1][col - 1]

            sums[row][col] = up + left - diagonalTopLeft + value


print(maximumSumSubmatrix(matrix, size))


"""
[
    [5, 8, 7, 12], 
    [-2, 4, 10, 19],
    [10, 24, 30, 39], 
    [11, 17, 15, 26]
]
"""
