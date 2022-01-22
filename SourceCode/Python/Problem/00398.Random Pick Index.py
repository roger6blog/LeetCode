'''
Level: Medium   Tag: [Random]

Given an integer array nums with possible duplicates, randomly output the index of a given target number.

You can assume that the given target number must exist in the array.

Implement the Solution class:

Solution(int[] nums) Initializes the object with the array nums.
int pick(int target) Picks a random index i from nums where nums[i] == target.
If there are multiple valid i's, then each index should have an equal probability of returning.


Example 1:

Input
["Solution", "pick", "pick", "pick"]
[[[1, 2, 3, 3, 3]], [3], [1], [3]]
Output
[null, 4, 0, 2]

Explanation
Solution solution = new Solution([1, 2, 3, 3, 3]);
solution.pick(3); // It should return either index 2, 3, or 4 randomly.
Each index should have equal probability of returning.
solution.pick(1); // It should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(3); // It should return either index 2, 3, or 4 randomly.
Each index should have equal probability of returning.


Constraints:

1 <= nums.length <= 2 * 10^4
-2^31 <= nums[i] <= 2^31 - 1
target is an integer from nums.
At most 10^4 calls will be made to pick.


'''



'''
取樣的關鍵在於對每個元素的選取需要是等概率的。
水塘取樣其目的在於從包含n個專案的集合S中選取k個樣本，其中n為一很大或未知的數量
尤其適用於不能把所有n個專案都存放到主記憶體的情況。
適用問題:
1.可否在一未知大小的集合中，隨機取出k個元素？
2.在不知道檔案總行數的情況下，如何從檔案中隨機的抽取k行？

step1.首先將前k個元素全部選取。
step2.對於第i個元素(i>k)，以概率k/i來決定是否保留該元素，如果保留該元素的話，
則隨機丟棄掉原有的k個元素中的一個(即原來某個元素被丟掉的概率是1/k)。
結果: 每個元素被最終被選取的概率都是k/n。
'''


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums


    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        import random
        if self.nums.count(target) == 1:
            return self.nums.index(target)

        ans = None
        count = 0
        for c, x in enumerate(self.nums):
            if x == target:
                count += 1
                chance = random.randint(1, count)
                if chance == 1:
                    ans = c
        return ans


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)

nums = [1, 2, 3, 3, 3]
obj = Solution(nums)
param_1 = obj.pick(3)
