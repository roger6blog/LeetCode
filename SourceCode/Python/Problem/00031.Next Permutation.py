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
    '''
    从最后一个位置开始，找到一个上升点，上升点之前的无需改动。
    然后，翻转上升点之后的降序。 在降序里，找到第一个比上升点大的，交换位置。
    看下面一个例子，有如下的一个数组

    1　　2　　7　　4　　3　　1

    下一个排列为：

    1　　3　　1　　2　　4　　7

    那么是如何得到的呢，我们通过观察原数组可以发现，如果从末尾往前看，数字逐渐变大，到了2时才减小的，
    然后再从后往前找第一个比2大的数字，是3，那么我们交换2和3，再把此时3后面的所有数字转置一下即可，步骤如下：

    1　　2　　7　　4　　3　　1

    1　　3　　7　　4　　2　　1

    1　　3　　1　　2　　4　　7
        '''
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
        def rec(res, index, nums, curr):
            curr_len = len(curr)
            num_len = len(nums)
            if curr_len == num_len:
                if curr not in res:
                    res.append(curr)
                    return

            elif curr_len > num_len:
                return

            for i in range(num_len):
                if i in index:
                    continue
                rec(res, index+[i], nums, curr+[nums[i]])


        candidate = []
        rec(candidate, [], nums, [])
        candidate.sort()

        next_perm = candidate.index(nums) + 1
        if next_perm == len(candidate):
            next_perm = 0
        for i in range(len(nums)):
            nums[i] = candidate[next_perm][i]

        print(nums)
        return


    def nextPermutation3(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        from itertools import permutations

        perms = list(set(list(permutations(nums))))
        perms.sort()
        next_perm = perms.index(tuple(nums)) + 1
        if next_perm == len(perms):
            next_perm = 0
        for i in range(len(nums)):
            nums[i] = perms[next_perm][i]

        print(nums)
        return

    def nextPermutation4(self, nums):
        n = len(nums)
        for i in range(n-1, -1, -1):
            if i > 0 and nums[i] > nums[i-1]:
                for j in range(n-1, i-1, -1):
                    if nums[j] > nums[i-1]:
                        nums[j], nums[i-1] = nums[i-1], nums[j]
                        nums = nums[:i] + nums[i:][::-1]
                        return nums

        return nums[::-1]

nums = [1,4,5,3,2]
nums2 = [3,2,1]
print(Solution().nextPermutation(nums2))
print(Solution().nextPermutation4(nums))
nums = [3,2,1]
print(Solution().nextPermutation3(nums))
nums = [1,4,5,3,2]
print(Solution().nextPermutation3(nums))
nums = [1,1,5]
print(Solution().nextPermutation3(nums))

nums = [2,2,7,5,4,3,2,2,1]  # TLE case
print(Solution().nextPermutation3(nums))

nums = [6,7,5,3,5,6,2,9,1,2,7,0,9] # MLE case, eat 2GB memory!
print(Solution().nextPermutation3(nums))