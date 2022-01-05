'''
Level: Easy

You are playing the following Flip Game with your friend: Given a string that contains only two characters:
 + and -, you can flip two consecutive "++" into "--",
 you can only flip one time. Please find all strings that can be obtained after one flip.

Write a program to find all possible states of the string after one valid move.


Example1

Input:  s = "++++"
Output:
[
  "--++",
  "+--+",
  "++--"
]

Example2

Input: s = "---+++-+++-+"
Output:
[
	"---+++-+---+",
	"---+++---+-+",
	"---+---+++-+",
	"-----+-+++-+"
]

'''

class Solution:
    def generatePossibleNextMoves(self, s):
        """
        @param s: the given string
        @return: all the possible states of the string after one valid move
        """
        import copy
        s = list(s)
        ans = []
        for i in range(len(s)):
            if  i+1 < len(s) and s[i] == "+" and s[i+1] == "+":
                t = copy.deepcopy(s)

                t[i] = "-"
                t[i+1] = "-"
                t = ''.join(t)
                ans.append(t)


        print(ans)
        return ans


s = "++++"
assert [
  "--++",
  "+--+",
  "++--"
] == Solution().generatePossibleNextMoves(s)

s = "---+++-+++-+"
assert [
    "-----+-+++-+",
    "---+---+++-+",
	"---+++---+-+",
    "---+++-+---+"
] == Solution().generatePossibleNextMoves(s)
