'''
Level: Medium   Tag: [Trie]

Design a data structure that supports adding new words
and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure
that matches word or false otherwise.
word may contain dots '.' where dots can be matched with any letter.


Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True


Constraints:

1 <= word.length <= 500
word in addWord consists lower-case English letters.
word in search consist of  '.' or lower-case English letters.
At most 50000 calls will be made to addWord and search.


'''




'''
基本仿造208題的Trie樹做法
但对于.符号，需要对当前节点的所有孩子进行遍历。
为此我们需要定一个新的函数，因为search函数只有要查找的字符串，肯定是以根节点root开始查的
而我们向后面查的过程中，一定会移动到子节点上，所以需要新的函数match。

'''


class TrieNode:
    def __init__(self):
        self.child = {}
        self.is_word = False
class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.root
        for c in word:
            if c not in curr.child:
                curr.child[c] = TrieNode()
            curr = curr.child[c]

        curr.is_word = True

    def match(self, word, index, root):
        if root == None:
            return False

        if index == len(word):
            return root.is_word

        if word[index] != '.':
            if root != None and self.match(word, index+1, root.child.get(word[index])):
                return True
            else:
                return False
        else:
            for child in root.child.values():
                if self.match(word, index+1, child):
                    return True
            return False


    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return self.match(word, 0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

word = "bad"
obj = WordDictionary()
obj.addWord(word)
param_2 = obj.search(word)
print(param_2)
print(obj.search("mad"))
assert False == obj.search("mad")
assert True == obj.search(".ad")