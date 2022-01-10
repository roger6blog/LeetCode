'''
Level: Medium

Given an array nums of n integers, r

eturn an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.



Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]


Constraints:

1 <= nums.length <= 200
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9

'''

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []
        candidate = []

        for x in range(len(nums)):
            # 節省重複計算
            if x >= 1 and nums[x] == nums[x-1]:
                continue
            for y in range(x+1, len(nums)):
                # 節省重複計算
                if y != x+1 and nums[y] == nums[y-1]:
                    continue
                t = target - nums[x] - nums[y]
                another_num_map = {}
                for i in range(len(nums)):
                    # 節省重複計算
                    if i in [x, y]:
                        continue
                    # 把排序去掉作最佳化 (sorted[nums[x], nums[y], nums[i] ,target-(nums[x]+nums[y]+nums[i])]) ==>
                    # [nums[x], nums[y], nums[i] ,target-(nums[x]+nums[y]+nums[i])]
                    if [nums[x], nums[y], nums[i] ,target-(nums[x]+nums[y]+nums[i])] in ans:
                        continue
                    if nums[i] not in another_num_map:
                        another_num_map[t - nums[i]] = i
                    else:
                        candidate = sorted([nums[x], nums[y], nums[i], nums[another_num_map[nums[i]]]])
                        if candidate not in ans:
                            ans.append(candidate)
                            # 節省重複計算
                            break
        print(ans)
        return ans

# nums = [1,0,-1,0,-2,2]
# target = 0
# Solution().fourSum(nums, target)


nums = [-3,-2,-1,0,0,1,2,3]
target = 0
Solution().fourSum(nums, target)
expect = [[-3,-2,2,3],[-3,-1,1,3],[-3,0,0,3],[-3,0,1,2],[-2,-1,0,3],[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]


nums = [2,2,2,2,2]
target = 8
Solution().fourSum(nums, target)

nums = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
target = 8






nums = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90]
target = 200

