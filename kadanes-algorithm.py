# time: O(n) | space: O(1)
def kadanesAlgorithm(A):
    maxEnding = A[0]
    maxSoFar = A[0]

    for i in range(1, len(A)):
        maxEnding = max(A[i], A[i] + maxEnding)
        maxSoFar = max(maxSoFar, maxEnding)
    return maxSoFar


array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(kadanesAlgorithm(array))

"""
# dry run
maxEnding = 5
maxSoFar = 6
-2, 1, -3, 4, -1, 2, 1, -5, 4
                            ^

maxEnding = max(4, 4 + 1) -> 5
"""
