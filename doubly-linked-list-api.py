class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # time: O(1) | space: O(1)
    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.insertBefore(self.head, node)

    # time: O(1) | space: O(1)
    def setTail(self, node):
        if self.tail is None:
            self.setHead(node)
            return
        self.insertAfter(self.tail, node)

    # time: O(1) | space: O(1)
    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert is self.head and nodeToInsert is self.tail:
            return
        self.remove(nodeToInsert)

        nodeToInsert.next = node
        nodeToInsert.prev = node.prev

        if node.prev is not None:
            node.prev.next = nodeToInsert
        else:
            self.head = nodeToInsert
        node.prev = nodeToInsert

    # time: O(1) | space: O(1)
    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert is self.head and nodeToInsert is self.tail:
            return
        self.remove(nodeToInsert)

        nodeToInsert.next = node.next
        nodeToInsert.prev = node

        if node.next is not None:
            node.next.prev = nodeToInsert
        else:
            self.tail = nodeToInsert
        node.next = nodeToInsert

    # time: O(n) | space: O(1)
    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
            return
        idx = 1
        node = self.head
        while node is not None and idx != position:
            node = node.next
            idx += 1
        if node is None:
            self.setTail()
        else:
            self.insertBefore(node, nodeToInsert)

    # time: O(n) | space: O(1)
    def removeNodesWithValue(self, value):
        node = self.head
        while node is not None:
            nodeToRemove = node
            node = node.next
            if value == nodeToRemove.value:
                self.remove(nodeToRemove)

    # time: O(1) | space: O(1)
    def remove(self, node):
        # set head or tail if nodeToRemove is head or tail
        if node is self.head:
            self.head = self.head.next
        if node is self.tail:
            self.tail = self.tail.prev

        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.next = None
        node.prev = None

    # time: O(n) | space: O(1)
    def containsNodeWithValue(self, value):
        node = self.head
        while node is not None:
            if value == node.value:
                return True
            node = node.next
        return False
