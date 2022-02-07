'''
Level: Medium  Tag: [String]

You are given an integer array nums that is sorted in non-decreasing order.

Determine if it is possible to split nums into one or more subsequences such that
both of the following conditions are true:

Each subsequence is a consecutive increasing sequence
(i.e. each integer is exactly one more than the previous integer).
All subsequences have a length of 3 or more.
Return true if you can split nums according to the above conditions, or false otherwise.

A subsequence of an array is a new array that is formed from the original array by deleting some
(can be none) of the elements without disturbing the relative positions of the remaining elements.
(i.e., [1,3,5] is a subsequence of [1,2,3,4,5] while [1,3,2] is not).



Example 1:

Input: nums = [1,2,3,3,4,5]
Output: true
Explanation: nums can be split into the following subsequences:
[1,2,3,3,4,5] --> 1, 2, 3
[1,2,3,3,4,5] --> 3, 4, 5

Example 2:

Input: nums = [1,2,3,3,4,4,5,5]
Output: true
Explanation: nums can be split into the following subsequences:
[1,2,3,3,4,4,5,5] --> 1, 2, 3, 4, 5
[1,2,3,3,4,4,5,5] --> 3, 4, 5

Example 3:

Input: nums = [1,2,3,4,4,5]
Output: false
Explanation: It is impossible to split nums into consecutive increasing subsequences of length 3 or more.


Constraints:

1 <= nums.length <= 10^4
-1000 <= nums[i] <= 1000
nums is sorted in non-decreasing order.

'''

'''
使用两个 HashMap, 第一个 HashMap 用来建立数字和其出现次数之间的映射 freq
第二个用来建立可以加在某个连续子序列后的数字与其可以出现的次数之间的映射 need。
对于第二个 HashMap, 举个例子来说, 就是假如有个连牌, 比如对于数字1,此时检测数字2和3是否存在, 若存在的话, 表明有连牌 [1,2,3] 存在
由于后面可以加上4, 组成更长的连牌, 所以不管此时牌里有没有4, 都可以建立 4->1 的映射, 表明此时需要一个4。

从最小的数字开始, 假设当前数字为num
    1.  先看看有没有数组以num - 1结尾, 有的话直接把num放过去, 然后以num - 1结尾的数组个数减1,
        以num为结尾的数组的个数加1, num的频率减1, 继续下一个数字
    2.  如果以num - 1结尾的数组个数不够了, 说明需要建立新的数组, 就要看num + 1和num + 2是否还有,
        有的话就建立新的数组, 此时多了一个以num + 2结尾的数组, 所以num + 2结尾的数组个数加1, 同时num + 1, num + 2的频率减1,
        最后num的频率也减1, 继续...
    3. 以上两点都不满足的话, 说明当前数字放不到任意一个已有的数组末尾, 并且也不能建立新的长度大于等于3的数组了, 返回False

'''


class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        from collections import Counter

        freq = Counter(nums)
        need = {}
        for n in nums:
            need[n] = 0


        for n in nums:
            if freq[n] == 0:
                continue

            if n-1 in need and need[n-1] > 0:
                need[n-1] -=1
                need[n] += 1
            elif n+1 in freq and n+2 in freq and freq[n+1] > 0 and freq[n+2] > 0:
                freq[n+1] -= 1
                freq[n+2] -= 1
                need[n+2] += 1
            else:
                return False

            freq[n] -= 1

        return True



    def isPossible_Wrong_Answer(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False

        ans = []
        n = len(nums)
        while nums.count(-1) < n-3 or len(nums) < 6:
            x = []
            for i in range(len(nums)):
                if nums[i] == -1:
                    continue
                if (not x or nums[i] - x[-1] == 1) and nums.count(-1) < n-3:
                    x.append(nums[i])
                    nums[i] = -1
            else:
                if len(x) < 3:
                    return False
                ans.append(x)
        last = []
        for i in range(len(nums)):
            if nums[i] == -1:
                continue
            if not last or nums[i] - last[-1] == 1:
                last.append(nums[i])
                nums[i] = -1
        else:
            ans.append(last)
        if nums.count(-1) != n:
            return False
        print(ans)
        return True



nums = [1,2,3,5,5,6,7]
assert False == Solution().isPossible(nums)
nums = [1,2,3,3,4,5]
assert True == Solution().isPossible(nums)
nums = [1,2,3,4,5]
assert True == Solution().isPossible(nums)