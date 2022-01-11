'''
Level: Medium  Tag: DFS
Given a string containing digits from 2-9 inclusive,
return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.

"../../../Material/Phone-Number.png"

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]


Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].


Note:
Although the above answer is in lexicographical order,
your answer could be in any order you want.

'''

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        def dfs(num, string, res):
            if num == length:    # Length is same as len(digits), done
                res.append(string)
                return
            for letter in dicTel[digits[num]]:
                dfs(num+1, string+letter, res)

        dicTel = {
            '2':['a', 'b', 'c'],
            '3':['d', 'e', 'f'],
            '4':['g', 'h', 'i'],
            '5':['j', 'k', 'l'],
            '6':['m', 'n', 'o'],
            '7':['p', 'q', 'r', 's'],
            '8':['t', 'u', 'v'],
            '9':['w', 'x', 'y', 'z']
        }

        res = []
        length = len(digits)
        if length == 0:
            return []
        dfs(0, '', res)
        return res










    def letterCombinations2(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """


        tel_map = {
            '2':['a', 'b', 'c'],
            '3':['d', 'e', 'f'],
            '4':['g', 'h', 'i'],
            '5':['j', 'k', 'l'],
            '6':['m', 'n', 'o'],
            '7':['p', 'q', 'r', 's'],
            '8':['t', 'u', 'v'],
            '9':['w', 'x', 'y', 'z']
        }


        def rec(res, letters, curr, digits):
            curr_len = len(curr)
            digit_len = len(digits)
            if curr_len == digit_len:
                res.append("".join(curr))
                return
            elif curr_len > digit_len:
                return
            for i in range(len(tel_map[digits[letters]])):
                rec(res, letters+1, curr+[tel_map[digits[letters]][i]], digits)



        ans = []
        if len(digits) == 0:
            return ans
        rec(ans, 0, [], digits)
        print(ans)

        return ans




digits = "23"
#Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
Solution().letterCombinations2(digits)