'''

Design a Tic-tac-toe game that is played between two players on a n x n grid.

You may assume the following rules:

A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves is allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.

Example:
Given n = 3, assume that player 1 is "X" and player 2 is "O" in the board.

TicTacToe toe = new TicTacToe(3);

toe.move(0, 0, 1); -> Returns 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

toe.move(0, 2, 2); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |

toe.move(2, 2, 1); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|

toe.move(1, 1, 2); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|

toe.move(2, 0, 1); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|

toe.move(1, 0, 2); -> Returns 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|

toe.move(2, 1, 1); -> Returns 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|
Follow up:
Could you do better than O(n2) per move() operation?


'''



class TicTacToeFast(object):
    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diag = 0
        self.obDiag = 0


    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        N = self.n
        add = 1 if player == 1 else -1

        self.rows[row] += add
        self.cols[col] += add

        if row == col:
            self.diag += add

        if row == self.n - col -1 :
            self.obDiag += add

        if abs(self.rows[row]) == N or abs(self.cols[col]) == N or abs(self.diag) == N or abs(self.obDiag) == N:
            print("Player {} win!!!".format(player))

class TicTacToe(object):
    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.n = n
        self.board = []
        for x in xrange(n):
            self.board.append([])
            for y in xrange(n):
                self.board[x].append(0)




    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """

        if self.board[row][col] != 0:
            print("You cannot move to this position: [{}][{}] occupied".format(row, col))

        self.board[row][col] = player
        rowLength = len(self.board)
        colLength = len(self.board[0])

        for i in xrange(colLength):
            if self.board[i].count(self.board[i][0]) == len(self.board[i]) and self.board[i][0] != 0:
                print("Player {} win!!!".format(self.board[i][0]))
                return self.board[i][0]

        winFlag = True
        for y in xrange(colLength):
            x = 0

            while x < rowLength-1:
                if self.board[x][y] != self.board[x+1][y]:
                    winFlag = False
                    break
                x += 1
            if winFlag and self.board[x][0] != 0:
                print("Player {} win!!!".format(self.board[x][0]))
                return self.board[x][y]

        diaWinFlag = True
        for x in xrange(rowLength-1):

            if self.board[x][x] != self.board[x+1][x+1]:
                diaWinFlag = False
                break
        if diaWinFlag and self.board[0][0] != 0:
            print("Player {} win!!!".format(self.board[0][0]))
            return self.board[0][0]

        obDiaWinFlag = True
        for x in xrange(rowLength-1):
            y = colLength-1
            if self.board[rowLength-1][y] != self.board[x][y-x]:
                obDiaWinFlag = False
                break
        if obDiaWinFlag and self.board[x][y] != 0:
            print("Player {} win!!!???".format(self.board[0][0]))
            return self.board[0][0]

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
n = 3
toe = TicTacToeFast(n)
toe.move(0, 0, 1)
toe.move(0, 2, 1)
toe.move(2, 2, 1)
toe.move(1, 2, 2)
toe.move(2, 0, 1)
toe.move(1, 1, 1)
# toe.move(0, 1, 2)
# toe.move(1, 0, 1)
# toe.move(1, 0, 2)
# toe.move(2, 1, 1)
print