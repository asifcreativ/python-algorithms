
class Heap:
    def __init__(self, array=[], compareFn=lambda a, b: a < b):  # default min heap
        self.compareFn = compareFn
        self.heap = self.heapify(array)
        self.length = len(array)

    def peek(self):
        return self.heap[0]

    def heapify(self, array):
        endIdx = len(array) - 1
        parentIdx = (endIdx - 1) // 2
        for idx in reversed(range(parentIdx + 1)):
            self.siftDown(idx, endIdx, array)
        return array

    def siftDown(self, parentIdx, endIdx, heap):
        leftChildIdx = parentIdx * 2 + 1
        while leftChildIdx <= endIdx:
            rightChildIdx = parentIdx * 2 + 2
            if rightChildIdx <= endIdx and self.compareFn(heap[rightChildIdx], heap[leftChildIdx]):
                idxToSwap = rightChildIdx
            else:
                idxToSwap = leftChildIdx
            if self.compareFn(heap[idxToSwap], heap[parentIdx]):
                self.swap(idxToSwap, parentIdx, heap)
                parentIdx = idxToSwap
                leftChildIdx = parentIdx * 2 + 1
            else:
                break

    def siftUp(self, childIdx, heap):
        parentIdx = (childIdx - 1) // 2
        while childIdx > 0 and self.compareFn(heap[childIdx], heap[parentIdx]):
            self.swap(childIdx, parentIdx, heap)
            childIdx = parentIdx
            parentIdx = (childIdx - 1) // 2

    def remove(self):
        self.swap(0, self.length - 1, self.heap)
        popped = self.heap.pop()
        self.length -= 1
        self.siftDown(0, self.length - 1, self.heap)
        return popped

    def insert(self, value):
        self.heap.append(value)
        self.length += 1
        childIdx = self.length - 1
        self.siftUp(childIdx, self.heap)

    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]


heap = Heap([8, 5, 2, 9, 5, 6, 3], lambda a, b: a > b)
# heap.remove()
# heap.remove()
print(heap.heap)
