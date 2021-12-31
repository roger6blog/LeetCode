'''
Level: Medium

According to the Wikipedia's article:
"The Game of Life, also known simply as Life,
is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells,
each cell has an initial state live (1) or dead (0).
Each cell interacts with its eight neighbors (horizontal, vertical, diagonal)
using the following four rules (taken from the above Wikipedia article):

1. Any live cell with fewer than two live neighbors dies,
as if caused by under-population.

2. Any live cell with two or three live neighbors lives on to the next generation.

3. Any live cell with more than three live neighbors dies,
as if by over-population..

4. Any dead cell with exactly three live neighbors becomes a live cell,
as if by reproduction.

Write a function to compute the next state (after one update) of the board given its current state.
The next state is created by applying the above rules simultaneously to every cell in the current state,
where births and deaths occur simultaneously.

Example:
"../../../Material/grid1.jpeg"
Input:
[
    [0,1,0],
    [0,0,1],
    [1,1,1],
    [0,0,0]
]
Output:
[
    [0,0,0],
    [1,0,1],
    [0,1,1],
    [0,1,0]
]

Example 2:
"../../../Material/grid2.jpeg"

Input: board = [
    [1,1],
    [1,0]
]
Output: [
    [1,1],
    [1,1]
]


Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 25
board[i][j] is 0 or 1.

Follow up:

Could you solve it in-place?
Remember that the board needs to be updated at the same time:
You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle,
the board is infinite, which would cause problems when the active area encroaches the border of the array.
How would you address these problems?

'''


import copy

# Use bit manipulation instead of extra space for board
DEAD_TO_DEAD = 0b00  # 0
LIVE_TO_LIVE = 0b01  # 1
LIVE_TO_DEAD = 0b10  # 2
DEAD_TO_LIVE = 0b11  # 3

class Solution(object):
    def countLiveNeighbors(self, i, j, row, col, board):
        # dx and xy mean the around coordinate of this node,
        # it should be 8 permutations
        dx = [1, 1,  1, 0,  0,-1,-1, -1]
        dy = [1, 0, -1, 1, -1, 1, 0, -1]
        cnt = 0
        for k in range(8):
            nx = i + dx[k]
            ny = j + dy[k]
            if nx < 0 or ny < 0 or nx >= row or ny >= col:
                continue
            if board[nx][ny] == 1:
                cnt += 1
        return cnt

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """

        temp = copy.deepcopy(board)

        row = len(board)
        col = len(board[0])
        for i in range(row):
            for j in range(col):
                cnt = self.countLiveNeighbors(i, j, row, col, temp)
                if temp[i][j] == 1:
                    if not (cnt == 2 or cnt == 3):
                        # cell will dead
                        board[i][j] = 0
                else:  # temp[i][j] ==0
                    if cnt == 3:
                        # cell will alive!
                        board[i][j] = 1


    def countLiveNeighborsFollowup(self, i, j, row, col, board):
        # dx and xy mean the around coordinate of this node,
        # it should be 8 permutations
        dx = [1, 1,  1, 0,  0,-1,-1, -1]
        dy = [1, 0, -1, 1, -1, 1, 0, -1]
        cnt = 0
        for k in range(8):
            nx = i + dx[k]
            ny = j + dy[k]
            if nx < 0 or ny < 0 or nx >= row or ny >= col:
                continue
            if board[nx][ny] == 1 or board[nx][ny] == LIVE_TO_DEAD:
                cnt += 1
        return cnt

    def gameOfLifeFollowup(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """



        row = len(board)
        col = len(board[0])
        for i in xrange(row):
            for j in xrange(col):
                cnt = self.countLiveNeighborsFollowup(i, j, row, col, board)
                if board[i][j] == 1:
                    if not (cnt == 2 or cnt == 3):
                        # cell will dead
                        board[i][j] = LIVE_TO_DEAD
                else:  # board[i][j] == 0
                    if cnt == 3:
                        # cell will alive!
                        board[i][j] = DEAD_TO_LIVE
        print(board)

        for i in range(row):
            for j in range(col):
                board[i][j] = board[i][j] & 1

Input= [
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
print(Input)
#Solution().gameOfLife(Input)
#print Input
Solution().gameOfLifeFollowup(Input)
print(Input)

Input = [
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,1,1,1,0],
    [0,1,1,1,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0]
]

Expect = [
    [0,0,0,0,0,0],
    [0,0,0,1,0,0],
    [0,1,0,0,1,0],
    [0,1,0,0,1,0],
    [0,0,1,0,0,0],
    [0,0,0,0,0,0]
]
Solution().gameOfLife(Input)
print(Input)