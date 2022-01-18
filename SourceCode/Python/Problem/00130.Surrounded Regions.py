'''
Leevel: Medium  Tag: [Matrix], [DFS]

Given an m x n matrix board containing 'X' and 'O',

capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.


Example 1:

"../../../Material/xogrid.jpg"

Input: board = [
    ["X","X","X","X"],
    ["X","O","O","X"],
    ["X","X","O","X"],
    ["X","O","X","X"]
    ]
Output: [
    ["X","X","X","X"],
    ["X","X","X","X"],
    ["X","X","X","X"],
    ["X","O","X","X"]
    ]
Explanation: Surrounded regions should not be on the border,
which means that any 'O' on the border of the board are not flipped to 'X'.
Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'.
Two cells are connected if they are adjacent cells connected horizontally or vertically.

Example 2:

Input: board = [["X"]]
Output: [["X"]]


Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is 'X' or 'O'.

'''

class Solution(object):
    def solve_TLE(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """


        def flip(board, x, y):
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
                return False

            if "?" in board[x][y] or board[x][y] == "X":
                return False

            if board[x][y] == "!":
                return True

            board[x][y] += "?"
            res = flip(board, x+1, y) or flip(board, x-1, y) or flip(board, x, y+1) or flip(board, x, y-1)
            board[x][y] = board[x][y][:1]

            return res

        m = len(board)
        n = len(board[0])

        for x in range(m):
            for y in range(n):
                if x == 0 or x == m-1:
                    if board[x][y] == "O":
                        board[x][y] = "!"
                if y == 0 or y == n-1:
                    if board[x][y] == "O":
                        board[x][y] = "!"

        for x in range(m):
            for y in range(n):
                if board[x][y] == "O":
                    if not flip(board, x, y):
                        board[x][y] = "X"

        for x in range(m):
            for y in range(n):
                if board[x][y] == "!":
                    board[x][y] = "O"
        print(board)

    '''
    先找出邊界的O，然後從邊界的O用DFS去找出鄰接他所有的O標記成*
    最後重新搜尋整個matrix，把所有被標記成*的元素都改成O
    '''

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        m = len(board)
        n = len(board[0])

        def flip(x, y):
            if x < 0 or x >= m or y < 0 or y >= n:
                return

            if board[x][y] != "O":
                return

            board[x][y] = "*"

            flip(x+1, y)
            flip(x-1, y)
            flip(x, y+1)
            flip(x, y-1)


        for x in range(m):
            for y in range(n):
                if x != 0 and y != 0 and x != m-1 and y != n-1:
                    continue
                if board[x][y] == "O":
                    flip(x, y)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '*':
                    board[i][j] = 'O'

        print(board)

board = [
    ["X","X","X","X"],
    ["X","O","O","X"],
    ["X","X","O","X"],
    ["X","O","X","X"]
    ]

Solution().solve(board)


board = [
    ["X","X","X"],
    ["X","O","X"],
    ["X","X","X"]
    ]
Solution().solve(board)