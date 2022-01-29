'''
Level: Medium  Tag: [Design]

Given an integer array nums, handle multiple queries of the following types:

Update the value of an element in nums.
Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
void update(int index, int val) Updates the value of nums[index] to be val.
int sumRange(int left, int right)
    Returns the sum of the elements of nums between indices left and right inclusive
    (i.e. nums[left] + nums[left + 1] + ... + nums[right]).


Example 1:

Input
["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
Output
[null, 9, null, 8]

Explanation
NumArray numArray = new NumArray([1, 3, 5]);
numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
numArray.update(1, 2);   // nums = [1, 2, 5]
numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8


Constraints:

1 <= nums.length <= 3 * 10^4
-100 <= nums[i] <= 100
0 <= index < nums.length
-100 <= val <= 100
0 <= left <= right < nums.length
At most 3 * 10^4 calls will be made to update and sumRange.


'''




'''
一道维护序列"单点修改, 区间查询"的模板题.

可以用树状数组, 区间树, 平衡树等数据结构解决.

而这道题目比较简单, 并且需要维护的区间信息为区间和(具有可加性, 可用前缀和相减求得区间和),

所以推荐使用树状数组: 一种简洁, 优美的数据结構


树状数组(Binary Index Tree) 是一种查询和修改复杂度均为 O(logn) 的数据结构。
这个树状数组比较有意思，所有的奇数位置的数字和原数组对应位置的相同，偶数位置是原数组若干位置之和
假如原数组 A(a1, a2, a3, a4 ...)，和其对应的树状数组 C(c1, c2, c3, c4 ...)有如下关系:


C1 = A1

C2 = A1 + A2

C3 = A3

C4 = A1 + A2 + A3 + A4

C5 = A5

C6 = A5 + A6

C7 = A7

C8 = A1 + A2 + A3 + A4 + A5 + A6 + A7 + A8

...

那么是如何确定某个位置到底是有几个数组成的呢，原来是根据坐标的最低位 Low Bit 来决定的，所谓的最低位，

就是二进制数的最右边的一个1开始，加上后面的0(如果有的话)组成的数字，例如1到8的最低位如下面所示:

坐标          二进制       最低位

1             0001          1

2             0010          2

3             0011          1

4             0100          4

5             0101          1

6             0110          2

7             0111          1

8             1000          8

...

最低位的计算方法有两种，一种是 x&(x^(x-1))，另一种是利用补码特性 x&-x。

这道题我们先根据给定输入数组建立一个树状数组 bit
比如，对于 nums = {1, 3, 5, 9, 11, 13, 15, 17}，建立出的 bit 数组为:

bit -> 0 1 4 5 18 11 24 15 74

注意到我们给 bit 数组开头 padding 了一个0，这样我们在利用上面的树状数组的性质时就不用进行坐标转换了。

可以发现bit数组中奇数位上的数字跟原数组是相同的，参见上面标记蓝色的数字。偶数位则是之前若干位之和，符合上图中的规律。

现在我们要更新某一位数字时，比如将数字5变成2，即 update(2, 2)，那么现求出差值 diff = 2 - 5 = -3

然后我们需要更新树状数组 bit，根据最低位的值来更新后面含有这一位数字的地方，一般只需要更新部分偶数位置的值即可。

由于我们在开头 padding了个0，所以我们的起始位置要加1，即 j=3，然后现将 bit[3] 更新为2，然后更新下一位

根据图中所示，并不是 bit[3] 后的每一位都需要更新的，下一位需要更新的位置的计算方法为 j += (j&-j)

这里我们的j是3，则 (j&-j) = 1，所以下一位需要更新的是 bit[4]，更新为15，现在j是4，则 (j&-j) = 4

所以下一位需要更新的是 bit[8]，更新为71，具体的变换过程如下所示:

0 1 4 5 18 11 24 15 74

0 1 4 2 18 11 24 15 74

0 1 4 2 15 11 24 15 74

0 1 4 2 15 11 24 15 71

接下来就是求区域和了，直接求有些困难，我们需要稍稍转换下思路。比如若我们能求出前i-1个数字之和，跟前j个数字之和，

那么二者的差值就是要求的区间和了。所以我们先实现求前任意i个数字之和，当然还是要利用树状数组的性质，

此时正好跟 update 函数反过来，我们的j从位置i开始，每次将 bit[j] 累加到 sum，然后更新j，通过 j -= (j&-j)，

这样就能快速的求出前i个数字之和，从而也就能求出任意区间之和了

'''





class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        n = len(nums)
        self.bit = [0] * (n+1)
        for i in range(n):
            self.add(i, nums[i])


    def add(self, index, val):
        index += 1
        while index <= len(self.nums):
            self.bit[index] += val
            index += self.lowbit(index)

    def lowbit(self, x):
        # x & (-x) 是為了找出binary value裡最低位的bit值 上面演算法已有解釋
        # 我們用888來當例子計算 x & (-x)
        # 888 的二進位值為 0000001101111000
        # 2'的補數        1111110010000111
        # 而其負數則為     1111110010001000 即2的補數+1
        # 所以對兩者做 AND 運算 即可找到最低位
        #                0000001101111000
        #             &  1111110010001000
        #             =              1000
        return x & (-x)

    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.add(index, val-self.nums[index])
        self.nums[index] = val


    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        def sum(index):
            index += 1
            ans = 0
            while index > 0:
                ans += self.bit[index]
                index -= self.lowbit(index)

            return ans

        return sum(right) - sum(left-1)



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

# nums = [1, 3, 5]
# obj = NumArray(nums)
# print(obj.sumRange(0, 2))
# obj.update(1, 2)
# print(obj.sumRange(0, 2))


# ["NumArray","sumRange","update","update","update","update","sumRange"]
# [[[5,18,13]],[0,2],[1,-1],[2,3],[0,5],[0,-4],[0,2]]

nums = [5,18,13]
obj = NumArray(nums)
print(obj.sumRange(0, 2))
obj.update(1, -1)
obj.update(2, 3)
obj.update(0, 5)
obj.update(0, -4)
print(obj.sumRange(0, 2))