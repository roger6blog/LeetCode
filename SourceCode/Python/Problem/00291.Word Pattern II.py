'''
Level: Medium

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match,
such that there is a bijection between a letter in pattern and a non-empty substring in str.
(i.e if a corresponds to s, then b cannot correspond to s.
For example, given pattern = "ab", str = "ss", return false.)

You may assume both pattern and str contains only lowercase letters.


Example 1

Input:
pattern = "abab"
str = "redblueredblue"
Output: true
Explanation: "a"->"red","b"->"blue"

Example 2

Input:
pattern = "aaaa"
str = "asdasdasdasd"
Output: true
Explanation: "a"->"asd"

Example 3

Input:
pattern = "aabb"
str = "xyzabcxzyabc"
Output: false


'''








'''


1. 本题和字模式I不同,题幹没有给出要配对的字符串,因此需要定义一个map类型dict来记录模板pattern中的字母对应配对的字符串,
    set类型used记录这个配对的字符串是否被枚举过。

2. 对输入的字符串str进行深度优先搜索，传入的参数包括：模板pattern、字符串str、dict、used

    a. 当pattern搜索到末尾且str也搜索到末尾即能完全匹配，返回true

    b. 如果当前模板的字母已经有匹配过字符串word:

如果word和现应匹配的str不匹配，则返回false
（例如模板为：ABA，字符串为abc，则搜索到第三位时A已经匹配过a，但现在str中是c无法匹配）

如果word和现应匹配的str匹配，则递归调用dfs并返回结果，步进为：pattern往后1位，str往后word的长度位数

    c. 如果当前模板的字母未匹配过字符串：

遍历整个str，枚举字符串前缀word的作为匹配

若当前的word在set中则证明其已经在b.步骤中完成，可以剪枝

将word加入dict和used

递归调用dfs并返回结果，步进为：pattern往后1位，str往后word长度位数

将word从dict和used中删除

若所有的word都无法匹配，返回false

复杂度分析
时间复杂度：O(lengthStr^lengthPattern)

每次递归有lengthStr种匹配串，一共有lengthPattern次，为指数级
空间复杂度：O(lengthPattern)


'''

class Solution:
    """
    @param pattern: a string,denote pattern string
    @param str: a string, denote matching string
    @return: a boolean
    """
    def wordPatternMatch(self, pattern, str):

        # write your code here

        # no accelerate version
        def basic_rec(ptn, string):
            # 能檢查的pattern都檢查完了
            if len(ptn) == 0:
                if len(string) == 0:
                    return True
                else:
                    # 還有沒match到的string
                    return False

            for i in range(len(string)):
                if basic_rec(ptn[1:], string[i+1:]):
                    return True

            return False




        def rec(ptn, string, ptn_map, used):
            if len(ptn) == 0:
                if len(string) == 0:
                    return True
                else:
                    return False

            # 取第一個字母當pattern
            p = ptn[0]

            if p in ptn_map:
                word = ptn_map[p]

                # 剪枝，發現字串開頭不對就馬上掉頭，加速遞迴過程
                if not string.startswith(word):
                    return False

                w = len(word)
                return rec(ptn[1:], string[w:], ptn_map, used)

            for i in range(len(string)):
                # 列舉可能匹配的字串
                word = string[i+1:]

                # 剪枝: 如果這word已經有被用過 就直接跳過 加速遞迴
                if word in used:
                    continue

                ptn_map[p] = word
                used.add(word)

                if rec(ptn[1:], string[i+1:], ptn_map, used):
                    return True

                used.remove(word)
                del ptn_map[p]
            return False

        used = set()
        ptn_map = {}
        ans = rec(pattern, str, ptn_map, used)
        # ans = basic_rec(pattern, str)
        print(ans)
        return ans


pattern = "abab"
str = "redblueredblue"
Solution().wordPatternMatch(pattern, str)

pattern = "aaaa"
str = "asdasdasdasd"
Solution().wordPatternMatch(pattern, str)