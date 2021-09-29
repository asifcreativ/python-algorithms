# find the kth smallest number in the array


# avg: time: O(n) | sapce: O(1)
# worst: time: O(n^2) | space: O(1)
def quickselect(array, k):
    k -= 1
    return quickSelectHelper(array, 0, len(array) - 1, k)


def quickSelectHelper(array, startIdx, endIdx, k):
    while startIdx <= endIdx:
        pivot = startIdx
        left = startIdx + 1
        right = endIdx
        while left <= right:
            if array[left] > array[pivot] and array[right] < array[pivot]:
                swap(left, right, array)
            if array[left] <= array[pivot]:
                left += 1
            if array[right] >= array[pivot]:
                right -= 1
        swap(pivot, right, array)

        if right == k:
            return array[k]
        elif right > k:
            endIdx = right - 1
        else:
            startIdx = right + 1


def swap(i, j, arr):
    arr[i], arr[j] = arr[j], arr[i]


print(quickselect([8, 1, 5, 2, -1, 9, 7, 6, 3, -4], 3))
print(quickselect([8, 1, 5, 2, -1, 9, 7, 6, 3, -4], 2))
