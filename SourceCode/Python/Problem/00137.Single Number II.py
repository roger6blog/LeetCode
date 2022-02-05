'''
Level: Medium  Tag:  [Bit Manipulation]

Given an integer array nums where every element appears three times except for one,

which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.



Example 1:

Input: nums = [2,2,3,2]
Output: 3

Example 2:

Input: nums = [0,1,0,1,0,1,99]
Output: 99


Constraints:

1 <= nums.length <= 3 * 10^4
-2^31 <= nums[i] <= 2^31 - 1
Each element in nums appears exactly three times except for one element which appears once.

'''



'''
由於其他數字會重複三次, XOR做三次會導致最後大家都出現在答案內, 所以要另外用東西紀錄「它出現兩次了」。
當然我們可以繼續利用XOR的作法, 用一個int紀錄出現第二次, 如果出現兩次就不加入找答案的數字。

我們逐一解釋一下流程

首先one, two的運作邏輯應該是這樣:

如果不在one或two內, 就塞進one內
如果在one內, 把one內的東西刪掉,再塞進two內
如果在two內, 就把two內的東西刪掉
實際上流程是:

先塞進one內XOR, 如果two內有的話, 把剛剛的動作取消
先塞進two內XOR, 如果one內有的話, 把剛剛的動作取消



& ~one和& ~two到底是幹嘛用的?

因為上面的程式碼一定會先把n丟進one及two內做XOR, 所以後面的東西是「如果不應該把n丟進去XOR, 就把前面的動作取消」

大家知道 1 & ~1 = 0 這件事對吧? (1和反1做AND會抵消)

& ~two就代表說, 如果n已經在one內, 而two中也有n, n就會被抵銷。因為two內的n變成了~n (反n)

& ~one相同, 如果n已經在two內, 而one中也有n, n就會被抵銷。因為one內的n變成了~n(反n)


所以說, 我們把{1,1,1}丟進去的話, one和two的變化應該要是
1.
one: 1
two: 0

2.
one: 0
two: 1

3.
one: 0
two: 0

'''


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one = 0
        two = 0

        for n in nums:
            one = (one^n) & ~two
            two = (two^n) & ~one

        print(one)
        return one


nums = [0,1,0,1,0,1,99]
Solution().singleNumber(nums)