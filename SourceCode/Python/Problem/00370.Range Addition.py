'''
Level: Medium      Tag: [Matrix], [Line sweep]

Assume you have an array of length n initialized with all 0's and are given k update operations.

Each operation is represented as a triplet:

[startIndex, endIndex, inc] which increments each element of subarray A[startIndex ... endIndex]
(startIndex and endIndex inclusive) with inc.

Return the modified array after all k operations were executed.



Given:
length = 5,
updates =
[
[1,  3,  2],
[2,  4,  3],
[0,  2, -2]
]
return [-2, 0, 3, 5, 3]

Explanation:
Initial state:
[ 0, 0, 0, 0, 0 ]
After applying operation [1, 3, 2]:
[ 0, 2, 2, 2, 0 ]
After applying operation [2, 4, 3]:
[ 0, 2, 5, 5, 3 ]
After applying operation [0, 2, -2]:
[-2, 0, 3, 5, 3 ]

'''

class Solution:
    """
    @param length: the length of the array
    @param updates: update operations
    @return: the modified array after all k operations were executed
    """
    # O (k*n) k 是update個數
    def getModifiedArray_TLE(self, length, updates):
        ans = [0 for _ in range(length)]
        for start, end, inc in updates:
            for i in range(start, end+1):
                ans[i] += inc

        print(ans)

        return ans



    """
    掃描線算法
    只是对每个区间的start 加上值， 在end + 1 减去值
    意思是，start开始每个坐标都 累加这个值
    而到了end + 1 开始这个值就要减去。
    即resi = resi - 1 + resi
    """
    # O (k+n) k 是update個數
    def getModifiedArray(self, length, updates):
        ans = [0 for _ in range(length)]

        oper = ans + [0]

        for start, end, inc in updates:
            oper[start] += inc
            oper[end+1] -= inc

        for i in range(len(ans)):
            if i == 0:
                ans[i] = oper[i]
            else:
                ans[i] = oper[i] + ans[i-1]

        print(ans)
        return ans

length = 5
updates = [
[1,  3,  2],
[2,  4,  3],
[0,  2, -2]
]
Solution().getModifiedArray(length, updates)