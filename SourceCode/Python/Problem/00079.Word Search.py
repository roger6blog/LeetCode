'''
Level: Medium   Tag: [Matrix], [DFS]

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell,

where "adjacent" cells are those horizontally or vertically neighboring.

The same letter cell may not be used more than once.

Example:

"../../../Material/word2.jpeg"

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.

Example2:

"../../../Material/word-1.jpeg"

Given word = "SEE", return true.

Example3:

"../../../Material/word3.jpeg"
Given word = "ABCB", return false.


'''


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        row = len(board)
        col = len(board[0])
        for x in xrange(row):
            for y in xrange(col):
                if self.dfs(board, word, x, y):
                    return True
        return False

    def dfs(self, board, word, x, y):
        if len(word) == 0:
            return True

        if x >= len(board) or x < 0:
            return False

        if y >= len(board[0]) or y < 0:
            return False



        if word[0] != board[x][y]:
            return False
        word = word[1:]
        board[x][y] = board[x][y].swapcase()
        res = self.dfs(board, word, x + 1, y) or \
              self.dfs(board, word, x - 1, y) or \
              self.dfs(board, word, x, y + 1) or \
              self.dfs(board, word, x, y - 1)

        board[x][y] = board[x][y].swapcase()
        return res


    def exist2(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """


        def rec(board, x, y, word, visit):
            if not len(word):
                return True

            row = len(board)
            col = len(board[0])
            if x < 0 or x >= row or y < 0 or y >= col:
                return False

            if (x, y) in visit:
                return False

            if word[0] != board[x][y]:
                return False

            word = word[1:]
            visit.add((x,y))
            ans = rec(board, x+1, y, word, visit) or \
                  rec(board, x-1, y, word, visit) or \
                  rec(board, x, y+1, word, visit) or \
                  rec(board, x, y-1, word, visit)

            visit.remove((x,y))
            return ans

        visit = set()
        row = len(board)
        col = len(board[0])
        for x in range(row):
            for y in range(col):
                if rec(board, x, y, word, visit):
                    return True

        return False

board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

board2 = [
    ['A', 'A']
]
word = "ABCCED"

word3 = "AAA"
# print(Solution().exist(board2, word3))
assert True == Solution().exist2(board, word)


word2 = "SEE"
assert True == Solution().exist2(board, word2)

board = [
    ["A","A"],
    ["A","a"],
    ["A","a"],
    ["a","a"],
    ["a","A"]
    ]
word = "AaaaaAaAA"
assert False == Solution().exist2(board, word)
