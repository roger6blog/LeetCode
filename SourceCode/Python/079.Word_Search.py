'''

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell,

where "adjacent" cells are those horizontally or vertically neighboring.

The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
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



        print word[0]
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



board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

board2 = [
    ['A', 'A']
]
word = "ABCCED"
word2 = "SEE"
word3 = "AAA"
print Solution().exist(board2, word3)