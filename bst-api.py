# the insert, contains, and remove methods.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return f"{self.value}"

    # average: time: O(log(n)) | space: O(1)
    # worst: time: O(n) | space: O(1)
    def insert(self, value):
        node = self
        while True:
            if value < node.value:
                if node.left is None:
                    node.left = BST(value)
                    break
                else:
                    node = node.left
            else:
                if node.right is None:
                    node.right = BST(value)
                    break
                else:
                    node = node.right
        return self

    # average: time: O(log(n)) | space: O(1)
    # worst: time: O(n) | space: O(1)
    def contains(self, value):
        node = self
        while node is not None:
            if value == node.value:
                return True
            if value < node.value:
                node = node.left
            else:
                node = node.right
        return False

    # average: time: O(log(n)) | space: O(1)
    # worst: time: O(n) | space: O(1)
    def remove(self, value, parent=None):
        node = self
        while node is not None:
            if value < node.value:
                parent = node
                node = node.left
            elif value > node.value:
                parent = node
                node = node.right
            else:  # nodeToRemove found
                # 1. nodeToRemove has both children's
                if node.left is not None and node.right is not None:
                    node.value = node.right.getMinValue()
                    node.right.remove(node.value, node)
                # 2. nodeToRemove has one child (left or right)
                # 2.1 nodeToRemove is root node
                elif parent is None:
                    if node.left is not None:
                        node.value = node.left.value
                        node.right = node.left.right
                        node.left = node.left.left
                    elif node.right is not None:
                        node.value = node.right.value
                        node.left = node.right.left
                        node.right = node.right.right
                    else:
                        pass  # single node tree
                # 2.2. nodeToRemove has one child (left or right) or no child
                elif node is parent.left:
                    parent.left = node.left if node.left is not None else node.right
                elif node is parent.right:
                    parent.right = node.left if node.left is not None else node.right
                break

        return self

    def getMinValue(self) -> int:
        node = self
        while node.left != None:
            node = node.left
        return node.value


# root
bst = BST(10)
# left subtree
bst.insert(5)
bst.insert(5)
bst.insert(2)
bst.insert(1)
# right subtree
bst.insert(15)
bst.insert(13)
bst.insert(22)
bst.insert(14)

bst.insert(12)

print(bst.contains(2))
print(bst.remove(10))
print(bst.contains(10))
