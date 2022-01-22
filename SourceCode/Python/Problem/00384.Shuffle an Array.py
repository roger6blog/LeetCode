'''
Level: Medium   Tag: [Random]

Given an integer array nums, design an algorithm to randomly shuffle the array.

All permutations of the array should be equally likely as a result of the shuffling.

Implement the Solution class:

Solution(int[] nums) Initializes the object with the integer array nums.
int[] reset() Resets the array to its original configuration and returns it.
int[] shuffle() Returns a random shuffling of the array.


Example 1:

Input
["Solution", "shuffle", "reset", "shuffle"]
[[[1, 2, 3]], [], [], []]
Output
[null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]

Explanation
Solution solution = new Solution([1, 2, 3]);
solution.shuffle();    // Shuffle the array [1,2,3] and return its result.
                       // Any permutation of [1,2,3] must be equally likely to be returned.
                       // Example: return [3, 1, 2]
solution.reset();      // Resets the array back to its original configuration [1,2,3]. Return [1, 2, 3]
solution.shuffle();    // Returns the random shuffling of array [1,2,3]. Example: return [1, 3, 2]



Constraints:

1 <= nums.length <= 200
-10^6 <= nums[i] <= 10^6
All the elements of nums are unique.
At most 5 * 10^4 calls in total will be made to reset and shuffle.


'''


class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums


    def reset(self):
        """
        :rtype: List[int]
        """
        return self.nums


    def shuffle(self):
        """
        :rtype: List[int]
        """
        import random
        nums = self.nums[:]
        for i in range(len(nums)):
            rand = random.randrange(i, len(nums))
            nums[i], nums[rand] = nums[rand], nums[i]
        print(nums)
        return nums



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
nums = [1, 2, 3]
obj = Solution(nums)
param_1 = obj.reset()
param_2 = obj.shuffle()