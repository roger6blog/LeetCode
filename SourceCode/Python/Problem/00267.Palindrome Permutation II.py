'''

Given a string s, return all the palindromic permutations (without duplicates) of it.

Return an empty list if no palindromic permutation could be form.


Example1

Input: s = "aabb"
Output: ["abba","baab"]

Example2

Input: "abc"
Output: []

'''
class Solution:
    """
    @param s: the given string
    @return: all the palindromic permutations (without duplicates) of it
    """
    def generatePalindromes(self, s):
        from collections import Counter, deque
        from itertools import permutations

        count = 0
        letter_map = Counter(s)
        odd_letter = ""
        even = ""
        for k, v in letter_map.items():
            if v % 2 == 1:
                count += 1
                odd_letter = k
            even += k * (v//2)

        if count > 1:
            return []

        p = permutations(even)
        ans = []
        curr = deque()
        if odd_letter:
            curr.append(odd_letter)


        for word in list(p):
            for w in word:
                curr.extendleft(w)
                curr.extend(w)
            ans.append("".join(curr))
            curr.clear()


        ans = list(set(ans))
        print(ans)
        return ans

s = "aabb"
Solution().generatePalindromes(s)

s = "daabb"
Solution().generatePalindromes(s)

s = "aaaabbbaaaa"
Solution().generatePalindromes(s)
s = "aabbb"
Solution().generatePalindromes(s)