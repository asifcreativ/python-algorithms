class MinMaxStack:
    def __init__(self):
        self.stack = []

    # time: O(1) | space: O(1)
    def peek(self):
        if not self.isEmpty():
            return self.stack[-1].value

    # time: O(1) | space: O(1)
    def pop(self):
        if not self.isEmpty():
            node = self.stack.pop()
            return node.value

    # time: O(1) | space: O(1)
    def push(self, number):
        if self.isEmpty():
            nodeToInsert = StackNode(number, number, number)
            self.stack.append(nodeToInsert)
            return
        topNode = self.stack[-1]
        minVal = min(number, topNode.minVal)
        maxVal = max(number, topNode.maxVal)
        nodeToInsert = StackNode(number, minVal, maxVal)
        self.stack.append(nodeToInsert)

    # time: O(1) | space: O(1)
    def getMin(self):
        if not self.isEmpty():
            return self.stack[-1].minVal

    # time: O(1) | space: O(1)
    def getMax(self):
        if not self.isEmpty():
            return self.stack[-1].maxVal

    def isEmpty(self):
        return len(self.stack) == 0


class StackNode:
    def __init__(self, value, minVal, maxVal):
        self.value = value
        self.minVal = minVal
        self.maxVal = maxVal
