'''
Level: Medium  Tag: [Matrix]

Determine if a 9 x 9 Sudoku board is valid.

Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.


Example 1:

"../../../Material/250px-Sudoku-by-L2G-20050714.svg.png"

Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true


Example 2:

Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8.
Since there are two 8's in the top left 3x3 sub-box, it is invalid.


Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.

'''

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        from collections import Counter
        def check_sudoku_totla(board, valid_sudoku):
            m = len(board)
            n = len(board[0])
            duplicate = []
            for x in range(m)            :
                for y in range(n):
                    if board[x][y] != "." and board[x][y] in duplicate:
                        valid_sudoku = False
                        return valid_sudoku
                    duplicate.append(board[x][y])
            return valid_sudoku

        def check_sudoku_line(board, valid_sudoku):
            m = len(board)
            n = len(board[0])
            rotate_board = [[board[j][i] for j in range(n)] for i  in range(m)[::-1]]
            for i in range(m):
                c = Counter(board[i])
                del c["."]
                for k, v in c.items():
                    if v > 1:
                        valid_sudoku = False

            for i in range(m):
                c = Counter(rotate_board[i])
                del c["."]
                for k, v in c.items():
                    if v > 1:
                        valid_sudoku = False

            return valid_sudoku

        m = len(board)
        n = len(board[0])

        valid_sudoku = True
        for x in range(3, n+3, 3):
            for y in range(3, n+3, 3):
                    small_board = [[board[i][j] for j in range(x-3, x)] for i in range(y-3, y) ]
                    valid_sudoku = check_sudoku_line(small_board, valid_sudoku)
                    valid_sudoku = check_sudoku_totla(small_board, valid_sudoku)

        if valid_sudoku:
            valid_sudoku = check_sudoku_line(board, valid_sudoku)

        return valid_sudoku



    '''
    1.查同row col是否有相同的数字
    2.查小框框是否有相同的数字 按从左到右从上到下，给每个小框框编号0-8， 代码：boxIndex = i // 3 * 3 + j // 3
    '''
    def isValidSudoku2(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool

        """
        no_dup_set = set()
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] != ".":
                    row = str(x) + "row-" + board[x][y]
                    col = str(y) + "col-" + board[x][y]
                    # box index: 分成9小格，每格長寬各3個，用來表示在哪個box裡
                    box_index = x // 3 * 3 + y // 3
                    box = str(box_index) + "box-" + board[x][y]
                    print(box)
                    if row in no_dup_set or col in no_dup_set or box in no_dup_set:
                        return False

                    no_dup_set.add(row)
                    no_dup_set.add(col)
                    no_dup_set.add(box)

        return True



# board = [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# assert True == Solution().isValidSudoku(board)

# board = [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# assert False == Solution().isValidSudoku(board)

board = [
    [".",".",".",".","5",".",".","1","."],
    [".","4",".","3",".",".",".",".","."],
    [".",".",".",".",".","3",".",".","1"],
    ["8",".",".",".",".",".",".","2","."],
    [".",".","2",".","7",".",".",".","."],
    [".","1","5",".",".",".",".",".","."],
    [".",".",".",".",".","2",".",".","."],
    [".","2",".","9",".",".",".",".","."],
    [".",".","4",".",".",".",".",".","."]]
assert False == Solution().isValidSudoku(board)
assert False == Solution().isValidSudoku2(board)
