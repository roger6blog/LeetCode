'''
Level: Medium   Tag: [String]

Sometimes people repeat letters to represent extra feeling. For example:

"hello" -> "heeellooo"
"hi" -> "hiiii"
In these strings like "heeellooo", we have groups of adjacent letters that are all the same:
    "h", "eee", "ll", "ooo".

You are given a string s and an array of query strings words.

A query word is stretchy if it can be made to be equal to s by any number of applications of
the following extension operation: choose a group consisting of characters c,
and add some number of characters c to the group so that the size of the group is three or more.

For example, starting with "hello", we could do an extension on the group "o" to get "hellooo",
but we cannot get "helloo" since the group "oo" has a size less than three.
Also, we could do another extension like "ll" -> "lllll" to get "helllllooo".
If s = "helllllooo", then the query word "hello" would be stretchy because of these two extension operations:
    query = "hello" -> "hellooo" -> "helllllooo" = s.
Return the number of query strings that are stretchy.



Example 1:

Input: s = "heeellooo", words = ["hello", "hi", "helo"]
Output: 1
Explanation:
We can extend "e" and "o" in the word "hello" to get "heeellooo".
We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.

Example 2:

Input: s = "zzzzzyyyyy", words = ["zzyy","zy","zyy"]
Output: 3


Constraints:

1 <= s.length, words.length <= 100
1 <= words[i].length <= 100
s and words[i] consist of lowercase letters.

'''

class Solution(object):
    def expressiveWords(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """

        def count_sequence(word):
            ret = []
            count = 1
            for i in range(1, len(word)):
                if word[i-1] == word[i]:
                    count += 1
                else:
                    ret.append((word[i-1], count))
                    count = 1
            ret.append((word[-1], count))
            return ret

        ans = 0
        c = count_sequence(s)

        char = 0
        count = 1

        for w in words:
            n = count_sequence(w)
            if len(n) != len(c):
                continue
            can_expand = True
            for i in range(len(n)):
                # 可以expand的條件有2:
                # 1. 同index的字元相同
                # 2. 同index的字元數相同或是s字串同index的字元數比較大而且超過3以上
                if not (n[i][char] == c[i][char] and \
                    (n[i][count] == c[i][count] or \
                    (c[i][count] > n[i][count] and c[i][count] >= 3))):
                    can_expand = False
            if can_expand:
                ans += 1
        print(ans)
        return ans







s = "heeellooo"
words = ["hello", "hi", "helo"]
assert 1 == Solution().expressiveWords(s, words)

s = "zzzzzyyyyy"
words = ["zzyy","zy","zyy"]
assert 3 == Solution().expressiveWords(s, words)

s = "sass"
words = ["sa"]
assert 0 == Solution().expressiveWords(s, words)