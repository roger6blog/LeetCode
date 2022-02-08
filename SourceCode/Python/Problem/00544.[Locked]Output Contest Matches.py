'''
Level: Medium

During the NBA playoffs, we always arrange the rather strong team to play with the rather weak team,

like make the rank 1 team play with the rank nth team,

which is a good strategy to make the contest more interesting.

Now, you're given n teams, and you need to output their final contest matches in the form of a string.

The n teams are given in the form of positive integers from 1 to n, which represents their initial rank.

(Rank 1 is the strongest team and Rank n is the weakest team.)

We'll use parentheses () and commas ,

to represent the contest team pairing - parentheses () for pairing and commas , for partition.

During the pairing process in each round, you always need to follow the strategy of making the rather
strong one pair with the rather weak one.


The n is in range [2, 2^12].
We ensure that the input n can be converted into the form 2^k, where k is a positive integer.

Example 1:

Input: 2
Output: "(1,2)"

Example 2:

Input: 4
Output: "((1,4),(2,3))"
Explanation:
  In the first round, we pair the team 1 and 4, the team 2 and 3 together,
  as we need to make the strong team and weak team together.
  And we got (1,4),(2,3).
  In the second round, the winners of (1,4) and (2,3) need to play again to generate the final winner,
  so you need to add the paratheses outside them.
  And we got the final answer ((1,4),(2,3)).

Example 3:

Input: 8
Output: "(((1,8),(4,5)),((2,7),(3,6)))"
Explanation:
  First round: (1,8),(2,7),(3,6),(4,5)
  Second round: ((1,8),(4,5)),((2,7),(3,6))
  Third round: (((1,8),(4,5)),((2,7),(3,6)))



'''

'''
先從數列兩端挑出每回合要比賽的隊伍組合
接著每兩個用括號合併在一起

'''

class Solution:
    """
    @param n: a integer, denote the number of teams
    @return: return a string
    """

    def findContestMatch(self, n):
        nums = [i+1 for i in range(n)]
        ans = []
        while nums:
            strong = nums.pop(0)
            weak = nums.pop()
            ans.append((strong, weak))

        while len(ans) > 1:
            x = ans[:]
            match = []
            while x:
                match.append(tuple(x[:2]))
                x = x[2:]
            ans = match

        print(match)

        return match

# n = 4
# Solution().findContestMatch(n)
n = 8
Solution().findContestMatch(n)