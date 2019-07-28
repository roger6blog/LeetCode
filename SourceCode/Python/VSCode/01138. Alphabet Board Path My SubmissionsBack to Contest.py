'''

'''


class Solution(object):
        def __init__(self):
            self.board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]

        def alphabetBoardPath(self, target):
            """
            :type target: str
            :rtype: str
            """
            def row(alpha):

                if alpha <= "e" and alpha >= "a":
                    return 0

                if alpha >= "f" and alpha <= "j":
                    return 1

                if alpha >= "k" and alpha <= "o":
                    return 2

                if alpha >= "p" and alpha <= "t":
                    return 3

                if alpha >= "u" and alpha <= "y":
                    return 4

                if alpha == "z":
                    return 5

                return -1 

            def col(alpha):
                if alpha == "z":
                    return 0

                for i in xrange(5):
                    for j in xrange(5):
                        if self.board[i][j] == alpha:
                            return j 

                return -1   
            ans = ""
            n = len(target)
            p = 0
            x = 0
            r = 0
            while p < n:
                if target[p] == "z":
                    while x < col(target[p]):
                        ans += "R"
                        x += 1

                    while x > col(target[p]):
                        ans += "L"
                        x -= 1

                    while r < row(target[p]):
                        ans += "D"
                        r += 1

                    while r > row(target[p]):
                        ans += "U"
                        r -= 1

                    ans += "!"
                    p += 1
                    continue



                while r < row(target[p]):
                    ans += "D"
                    r += 1

                while r > row(target[p]):
                    ans += "U"
                    r -= 1

                while x < col(target[p]):
                    ans += "R"
                    x += 1

                while x > col(target[p]):
                    ans += "L"
                    x -= 1
                ans += "!"
                p += 1
                

            return ans

print Solution().alphabetBoardPath("zb")