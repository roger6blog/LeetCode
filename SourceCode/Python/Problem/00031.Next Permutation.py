'''
Level: Medium

Implement next permutation,

which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible,

it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples.

Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 -> 1,3,2

3,2,1 -> 1,2,3

1,1,5 -> 1,5,1

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100

'''


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            return nums

        begin = -1
        change = 0
        for i in xrange(len(nums)-1, -1, -1):
            if i != len(nums)-1 and nums[i] < nums[i+1]:
                begin = i

                break

        if begin == -1:
            nums.reverse()
            #nums = nums[::-1] # Leetcode can't accept this!
            return nums
        else:
            for j in xrange(len(nums) - 1, -1, -1):
                if nums[j] > nums[begin]:
                    change = j
                    break

            print("begin = {}".format(begin))
            print("change = {}".format(change))
            nums[begin], nums[change] = nums[change], nums[begin]
            #nums = nums[:begin+1] + nums[begin+1:][::-1]  # Leetcode can't accept this!
            nums[begin + 1:len(nums)] = nums[begin + 1:len(nums)][::-1]
            return nums






    def nextPermutation2(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def rec(res, index, nums, curr, used):
            print(len(res))
            curr_len = len(curr)
            num_len = len(nums)
            if curr_len == num_len:
                if curr not in res:
                    res.append(curr[:])
                    return

            elif curr_len > num_len:
                return

            for i in range(num_len):
                if i in index:
                    continue

                if used[i] == True:
                    continue

                used[i] = True
                curr.append(nums[i])
                rec(res, index+[i], nums, curr, used)
                curr.pop()
                used[i] = False

        used = [False] * len(nums)
        candidate = []
        rec(candidate, [], nums, [], used)
        candidate.sort()

        next_perm = candidate.index(nums) + 1
        if next_perm == len(candidate):
            next_perm = 0
        for i in range(len(nums)):
            nums[i] = candidate[next_perm][i]

        print(nums)
        return



nums = [1,4,5,3,2]
nums2 = [3,2,1]
print(Solution().nextPermutation(nums2))

# nums = [3,2,1]
# print(Solution().nextPermutation2(nums))
# nums = [1,4,5,3,2]
# print(Solution().nextPermutation2(nums))
nums = [1,1,5]
print(Solution().nextPermutation2(nums))
nums = [2,2,7,5,4,3,2,2,1]
print(Solution().nextPermutation2(nums))