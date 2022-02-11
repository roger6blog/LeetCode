'''
Level: Medium  Tag: [Trie]


A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and
retrieve keys in a dataset of strings.
There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before),
and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word
that has the prefix prefix, and false otherwise.


Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True


Constraints:

1 <= word.length, prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3 * 10^4 calls in total will be made to insert, search, and startsWith.



========  Old Description  =========


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

'''
Trie explain:
一个保存了8个键的trie结构
"A", "to", "tea", "ted", "ten", "i", "in", and "inn", 如下图所示

"../../../Material/208_trie.png"

字典树主要有如下三点性质:

1. 根节点不包含字符, 除根节点以外每个节点只包含一个字符。

2. 从根节点到某一个节点, 路径上经过的字符连接起来, 为该节点对应的字符串。

3. 每个节点的所有子节点包含的字符串不相同

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


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
class Trie2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()


    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        curr = self.root
        # 順著root往下找有沒有字元c在hashmap裏
        # 有的話就繼續找
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_word = True


    def find(self, word):
        curr = self.root
        # 順著root試著去get每個char, 有的話就繼續往下找
        # 迴圈跑完後返回目前指的node供search和startwith判斷
        for c in word:
            curr = curr.children.get(c)
            if curr is None:
                return None
        return curr


    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curr = self.find(word)
        if curr is not None and curr.is_word == True:
            return True


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        return self.find(prefix) is not None


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

word = 'apple'
obj = Trie()
print(obj.startsWith('a'))

obj.insert(word)
param_2 = obj.search(word)
print(param_2)

word = 'apple'
obj = Trie2()
print(obj.startsWith('a'))

obj.insert(word)
param_2 = obj.search(word)
print(param_2)