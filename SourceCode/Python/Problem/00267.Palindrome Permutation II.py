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