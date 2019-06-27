'''

Suppose you have N integers from 1 to N.

We define a beautiful arrangement as an array that is constructed by these N numbers successfully if one of the following is true for the ith position (1 <= i <= N) in this array:

1. The number at the i-th position is divisible by i.

2. i is divisible by the number at the ith position.

Now given N, how many beautiful arrangements can you construct?

Example 1:
Input: 2
Output: 2
Explanation:

The first beautiful arrangement is [1, 2]:

Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).

Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).

The second beautiful arrangement is [2, 1]:

Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).

Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.

Note:
N is a positive integer and will not exceed 15.


'''


class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        used = [0] * (N + 1)
        self.count = 0
        self.perm(N, 1, used)
        return self.count

    def perm(self, N, index, used):
        if index > N:
            self.count += 1
            return
        for i in xrange(1, N + 1):
            if used[i] == 0 and (i % index == 0 or index % i == 0):
                print("Choose {}".format(i))
                used[i] = 1
                self.perm(N, index + 1, used)
                used[i] = 0



class Solution_TLE(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        nums = []
        ans = []
        for i in xrange(N):
            nums.append(i+1)

        self.exhaustive(nums, 0, ans)
        return ans

    def exhaustive(self, nums, index, ans):
        # print nums
        if index >= len(nums):
            for i in xrange(len(nums)):
                if (i+1) % nums[i] != 0 and nums[i] % (i+1) != 0:
                    return
            if nums not in ans:
                ans.append(nums[:])
        else:
            for i in xrange(index, len(nums)):
                nums[i], nums[index] = nums[index], nums[i]
                self.exhaustive(nums, index+1, ans)
                nums[index], nums[i] = nums[i], nums[index]




n = 3

print Solution_TLE().countArrangement(n)