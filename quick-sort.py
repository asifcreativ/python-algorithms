# avg: time: O(nlog(n)) | space: O(nlog(n))
# worst: time: O(n^2) | space: O(nlog(n))
def quickSort(array):
    quickSortHelper(array, 0, len(array) - 1)
    return array


def quickSortHelper(array, startIdx, endIdx):
    if startIdx >= endIdx:
        return
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
    isLeftSmaller = abs(right - 1 - startIdx) < abs(endIdx - right - 1)
    if isLeftSmaller:
        quickSortHelper(array, startIdx, right - 1)
        quickSortHelper(array, right + 1, endIdx)
    else:
        quickSortHelper(array, right + 1, endIdx)
        quickSortHelper(array, startIdx, right - 1)


def swap(i, j, arr):
    arr[i], arr[j] = arr[j], arr[i]


print(quickSort([8, 5, 2, -8, 9, 5, 6, 3, -3]))
