'''
Level: Medium

This question is about implementing a basic elimination algorithm for Candy Crush.

Given a 2D integer array board representing the grid of candy,
different positive integers board[i][j] represent different types of candies.

A value of board[i][j] = 0 represents that the cell at position (i, j) is empty.

The given board represents the state of the game following the player's move.

Now, you need to restore the board to a stable state by crushing candies according to the following rules:

If three or more candies of the same type are adjacent vertically or horizontally,
    "crush" them all at the same time - these positions become empty.
After crushing all candies simultaneously,
    if an empty space on the board has candies on top of itself,
    then these candies will drop until they hit a candy or bottom at the same time.
    (No new candies will drop outside the top boundary.)
After the above steps, there may exist more candies that can be crushed.
If so, you need to repeat the above steps.
If there does not exist more candies that can be crushed (ie. the board is stable), then return the current board.
You need to perform the above rules until the board becomes stable, then return the current board.


The length of board will be in the range [3, 50].
The length of board[i] will be in the range [3, 50].
Each board[i][j] will initially start as an integer in the range [1, 2000].


Example 1:

Input:
[
    [110,5,112,113,114],
    [210,211,5,213,214],
    [310,311,3,313,314],
    [410,411,412,5,414],
    [5,1,512,3,3],
    [610,4,1,613,614],
    [710,1,2,713,714],
    [810,1,2,1,1],
    [1,1,2,2,2],
    [4,1,4,4,1014]
    ]
Output:
[
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [110,0,0,0,114],
    [210,0,0,0,214],
    [310,0,0,113,314],
    [410,0,0,213,414],
    [610,211,112,313,614],
    [710,311,412,613,714],
    [810,411,512,713,1014]
]
Explanation

"../../../Material/0060lm7Tly1fp5kkl8ctij30ll0eswh7.jpg"

Example 2:

Input: [
    [1,3,5,5,2],
    [3,4,3,3,1],
    [3,2,4,5,2],
    [2,4,4,5,5],
    [1,4,4,1,1]
    ]
Output: [
    [1,3,0,0,0],
    [3,4,0,5,2],
    [3,2,0,3,1],
    [2,4,0,5,2],
    [1,4,3,1,1]
    ]

'''

'''
大题框架就是: 搜寻可以消除的块, 如果没有则局面稳定, 反之消除, 下落, 继续搜寻.

不过需要注意几个细节:

L型或者是十字型的可消除块要求的是行/列都需要至少3个相同的糖果
下落之后上方的空位补零
你不能只找到一个可以消除的块就立即消除然后下落, 而是找到当前局面中所有可以消除的块, 一次性消除, 然后下落,
这样才到达下一个局面, 再次判断.

我们可以这样实现: 因为给定的类型都是正数, 所以我们可以在一次搜寻中, 把所有可消除的块都转换成负数.

这样, 遍历整个地图完成一次搜寻后, 负数的块代表的就是可消除的, 置为0然后处理下落即可.

'''


class Solution:
    """
    @param board: a 2D integer array
    @return: the current board
    """

    def candyCrush(self, board):
        M = len(board)
        N = len(board[0])
        i = 0
        found = True
        while found:
            found = False
            for x in range(M):
                for y in range(N):
                    v = abs(board[x][y])
                    if v == 0:
                        continue
                    if x + 2 < M and board[x+1][y] == v and board[x+2][y] == v:
                        found = True
                        i = x
                        while i < M and board[i][y] == v:
                            board[i][y] = -v
                            i += 1
                    if y + 2 < N and board[x][y+1] == v and board[x][y+2] == v:
                        found = True
                        i = y
                        while i < N and board[x][i] == v:
                            board[x][i] = -v
                            i += 1
            # 處理落下的candy
            if found:
                # 逐列檢查
                for y in range(N):
                    i = M-1
                    for x in range(i, -1, -1):
                        # 如果該元素小於零，代表即將被取代，不會進入迴圈
                        # i不會減少，就能保留到落下後補零的迴圈數
                        if board[x][y] > 0:
                            board[i][y] = board[x][y]
                            i -= 1
                    # 落下後補零，如果i扣到0以下代表不用補零
                    for j in range(i, -1, -1):
                        board[j][y] = 0

        print(board)
        return board




candy = [
    [1,3,5,5,2],
    [3,4,3,3,1],
    [3,2,4,5,2],
    [2,4,4,5,5],
    [1,4,4,1,1]
    ]

Solution().candyCrush(candy)

candy = [
    [110,5,112,113,114],
    [210,211,5,213,214],
    [310,311,3,313,314],
    [410,411,412,5,414],
    [5,1,512,3,3],
    [610,4,1,613,614],
    [710,1,2,713,714],
    [810,1,2,1,1],
    [1,1,2,2,2],
    [4,1,4,4,1014]
    ]
Solution().candyCrush(candy)