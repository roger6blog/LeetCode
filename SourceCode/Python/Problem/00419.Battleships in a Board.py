'''
Level: Medium

Given an m x n matrix board where each cell is a battleship 'X' or empty '.',

return the number of the battleships on board.

Battleships can only be placed horizontally or vertically on board.

In other words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column),

where k can be of any size. At least one horizontal or vertical cell separates between two battleships

(i.e., there are no adjacent battleships).



Example 1:

"../../../Material/battelship-grid.jpg"


Input: board = [
    ["X",".",".","X"],
    [".",".",".","X"],
    [".",".",".","X"]]
Output: 2

Example 2:

Input: board = [["."]]
Output: 0


Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is either '.' or 'X'.


Follow up: Could you do it in one-pass, using only O(1) extra memory and without modifying the values board?

'''


'''
類似Number of Island, 但是用兩個變數 vertical horizontal
用 |= 來分別記錄每一個連續的x 和 y
如果有不同的row 或 col的x 或y被 |= 了，那x和y最後一定不會是原本同一行/列的值
如此便可依此判斷這些X是否在同一行/同一列上
'''


class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        visit = set()
        m = len(board)
        n = len(board[0])
        def rec(x, y, board):
            global vertical
            global horizontal
            if x < 0 or x >= m or y < 0 or y >= n:
                return

            if ((x, y)) in visit:
                return

            if board[x][y] == ".":
                return

            vertical |= x
            horizontal |= y
            visit.add((x, y))
            rec(x+1, y, board)
            rec(x-1, y, board)
            rec(x, y+1, board)
            rec(x, y-1, board)


        ans = 0
        for x in range(m):
            for y in range(n):
                if board[x][y] == 'X' and (x, y) not in visit:
                    global horizontal
                    horizontal = 0
                    global vertical
                    vertical = 0
                    rec(x, y, board)
                    if vertical == x or horizontal == y:
                        ans += 1

        print(ans)
        return ans


board = [["X","X","X"]]
Solution().countBattleships(board)

board = [
    ["X",".",".","X"],
    [".",".",".","X"],
    [".",".",".","X"]]
Solution().countBattleships(board)
