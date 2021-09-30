# best, avg, worst: time: O(nlog(n)) | space: O(1)
def heapSort(array):
    heapify(array)
    for endIdx in reversed(range(1, len(array))):
        swap(0, endIdx, array)
        siftDown(0, endIdx - 1, array)
    return array


def heapify(array):
    endIdx = len(array) - 1
    parentIdx = (endIdx - 1) // 2
    for idx in reversed(range(parentIdx + 1)):
        siftDown(idx, endIdx, array)


def siftDown(parentIdx, endIdx, heap):
    leftChildIdx = parentIdx * 2 + 1
    while leftChildIdx <= endIdx:
        rightChildIdx = parentIdx * 2 + 2
        if rightChildIdx <= endIdx and heap[rightChildIdx] > heap[leftChildIdx]:
            idxToSwap = rightChildIdx
        else:
            idxToSwap = leftChildIdx
        if heap[idxToSwap] > heap[parentIdx]:
            swap(idxToSwap, parentIdx, heap)
            parentIdx = idxToSwap
            leftChildIdx = parentIdx * 2 + 1
        else:
            break


def swap(i, j, heap):
    heap[i], heap[j] = heap[j], heap[i]


array = [8, 5, 2, 9, 5, 6, 3]
print(heapSort(array))
