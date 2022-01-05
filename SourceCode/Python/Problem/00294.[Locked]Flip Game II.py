'''
Level: Easy  Tag: [Back Tracking]

You are playing the following Flip Game with your friend:

Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--".

The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to determine if the starting player can guarantee a win.

Example1

Input:  s = "++++"
Output: true
Explanation:
The starting player can guarantee a win by flipping the middle "++" to become "+--+".

Example2

Input: s = "+++++"
Output: false
Explanation:
The starting player can not win
"+++--" --> "+----"
"++--+" --> "----+"

Follow up:

Derive your algorithm's runtime complexity.

'''
class Solution:
    memo = {}
    def canWin(self, s):
        """
        @param s: the given string
        @return: if the starting player can guarantee a win
        """

        if s in self.memo:
            return self.memo[s]

        for i in range(len(s)-1):
            if s[i:i+2] == "++":
                next_hand = s[:i] + "--" + s[i+2:]
                self.memo[next_hand] = self.canWin(next_hand)
                if self.memo[next_hand] == False:  # Enemy cannot win
                    return True                    # Player can win

        return False

'''
这道题是之前那道 Flip Game 的拓展，让我们判断先手的玩家是否能赢，可以穷举所有的情况，用回溯法来解题
思路跟上面那题类似，也是从第二个字母开始遍历整个字符串，
如果当前字母和之前那个字母都是+，那么递归调用将这两个位置变为--的字符串，如果返回 false，说明当前玩家可以赢，结束循环返回 false。

这里同时贴上热心网友 iffalse 的解释，这道题不是问 “1p是否会怎么选都会赢”，而是 “如果1p每次都选特别的两个+，最终他会不会赢”。
所以 canWin 这个函数的意思是 “在当前这种状态下，至少有一种选法，能够让他赢”。
而 (!canWin) 的意思就变成了 “在当前这种状态下，无论怎么选，都不能赢”。
所以 1p 要看的是，是否存在这样一种情况，无论 2p 怎么选，都不会赢。
所以只要有一个 (!canWin)，1p 就可以确定他会赢。这道题从博弈论的角度会更好理解。
每个 player 都想让自己赢，所以每轮他们不会随机选+。
每一轮的 player 会选能够让对手输的+。如果无论如何都选不到让对手输的+，那么只能是当前的 player 输了
'''


s = "++++"
assert True == Solution().canWin(s)
s = "+++++"
assert False == Solution().canWin(s)