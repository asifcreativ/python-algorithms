class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    # time: O(n^2) | space: O(n^2)
    def populateSuffixTrieFrom(self, string):
        for i in range(len(string)):
            self.insert(i, string)

    def insert(self, startIdx, string):
        node: dict = self.root
        for i in range(startIdx, len(string)):
            char = string[i]
            if char not in node:
                node[char] = {}
            node = node[char]
        node[self.endSymbol] = True

    # time: O(n) | space: O(1)
    def contains(self, string):
        node: dict = self.root
        for char in string:
            if char not in node:
                return False
            node = node[char]
        return self.endSymbol in node


tri = SuffixTrie("hello")
print(tri.contains("llo"))  # result True
print(tri.contains("world"))  # result False
tri2 = SuffixTrie("aaaaaaaa")
print(tri2.contains("a"))
