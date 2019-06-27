'''
# Time:  O(n), per operation
# Space: O(1)
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.


'''


class Trie(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.child = {}
        self.isWord = False

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        curr = self
        for i in word:
            if i not in curr.child:
                curr.child[i] = Trie()
            curr = curr.child[i]
        curr.isWord = True


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curr = self
        if curr.child is {}:
            return False
        for i in word:
            curr = curr.child.get(i)
            if curr is None:
                return False
        return curr.isWord

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curr = self
        for i in prefix:
            curr = curr.child.get(i)
            if curr is None:
                return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

word = 'apple'
obj = Trie()
print obj.startsWith('a')

obj.insert(word)
param_2 = obj.search(word)
print param_2