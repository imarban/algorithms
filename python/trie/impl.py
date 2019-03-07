class TrieNode(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = [False] * 26
        self.leaf = False


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """

        node = self.root
        for c in word:
            position = ord(c) - ord('a')
            if not node.children[position]:
                node.children[position] = TrieNode()

            node = node.children[position]

        node.leaf = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root

        for c in word:
            position = ord(c) - ord('a')
            if not node.children[position]:
                return False
            node = node.children[position]

        return node.leaf

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for c in prefix:
            position = ord(c) - ord('a')
            if not node.children[position]:
                return False
            node = node.children[position]

        return True

        # Your Trie object will be instantiated and called as such:
        # trie = Trie()
        # trie.insert("somestring")
        # trie.search("key")


trie = Trie()
trie.insert("app")
trie.insert("apple")
trie.insert("beer")
trie.insert("add")
trie.insert("jam")
trie.insert("rental")

print trie.search("apps")
print trie.search("app")
print trie.search("ad")
print trie.search("applepie")
print trie.search("rest")
print trie.search("jan")
print trie.search("rent")
print trie.search("beer")
print trie.search("jam")

print "------"

print trie.startsWith("apps")
print trie.startsWith("app")
print trie.startsWith("ad")
print trie.startsWith("applepie")
print trie.startsWith("rest")
print trie.startsWith("jan")
print trie.startsWith("rent")
print trie.startsWith("beer")
print trie.startsWith("jam")