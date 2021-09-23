class MinHeap:
    def __init__(self, array):
        self.heap = self.heapify(array)

    # time: O(n) | space: O(1)
    def heapify(self, array):
        endIdx = len(array) - 1
        lastParentIdx = (endIdx - 1) // 2
        for parentIdx in reversed(range(lastParentIdx + 1)):
            self.siftDown(parentIdx, endIdx, array)
        return array

    # time: O(log(n)) | space: O(1)
    def siftDown(self, parentIdx, endIdx, heap):
        leftChildIdx = parentIdx * 2 + 1
        while leftChildIdx <= endIdx:
            rightChildIdx = parentIdx * 2 + 2
            if rightChildIdx <= endIdx and heap[rightChildIdx] < heap[leftChildIdx]:
                idxToSwap = rightChildIdx
            else:
                idxToSwap = leftChildIdx
            if heap[idxToSwap] < heap[parentIdx]:
                self.swap(parentIdx, idxToSwap, heap)
                parentIdx = idxToSwap
                leftChildIdx = parentIdx * 2 + 1
            else:
                break

    # time: O(log(n)) | space: O(1)

    def siftUp(self, childIdx, heap):
        parentIdx = (childIdx - 1) // 2
        while parentIdx >= 0 and heap[childIdx] < heap[parentIdx]:
            self.swap(parentIdx, childIdx, heap)
            childIdx = parentIdx
            parentIdx = (childIdx - 1) // 2

    # time: O(1) | space: O(1)
    def peek(self):
        return self.heap[0]

    # time: O(log(n)) | space: O(1)
    def remove(self):
        endIdx = len(self.heap) - 1
        self.swap(0, endIdx, self.heap)
        popped = self.heap.pop()
        self.siftDown(0, endIdx - 1, self.heap)
        return popped

    # time: O(log(n)) | space: O(1)
    def insert(self, value):
        self.heap.append(value)
        endIdx = len(self.heap) - 1
        self.siftUp(endIdx, self.heap)

    # time: O(1) | space: O(1)
    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]


heap = MinHeap([8, 12, 24, 18, 31, 30, 44, 112, 19])
print(heap.peek())
heap.insert(3)
print(heap.peek())
