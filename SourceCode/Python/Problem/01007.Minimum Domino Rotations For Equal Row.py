'''
Level: Medium  Tag: [Greed]

In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino.
(A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

Return the minimum number of rotations so that all the values in tops are the same,
or all the values in bottoms are the same.

If it cannot be done, return -1.



Example 1:

"../../../Material/domino.png"

Input: tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
Output: 2
Explanation:
The first figure represents the dominoes as given by tops and bottoms: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2,
as indicated by the second figure.

Example 2:

Input: tops = [3,5,1,2,3], bottoms = [3,6,3,3,4]
Output: -1
Explanation:
In this case, it is not possible to rotate the dominoes to make one row of values equal.


Constraints:

2 <= tops.length <= 2 * 10^4
bottoms.length == tops.length
1 <= tops[i], bottoms[i] <= 6


'''

class Solution(object):
    def minDominoRotations(self, tops, bottoms):
        """
        :type tops: List[int]
        :type bottoms: List[int]
        :rtype: int
        """
        from collections import Counter
        t = Counter(tops)
        b = Counter(bottoms)
        from_top = True
        if t.most_common(1)[0][1] > b.most_common(1)[0][1]:
            target, _ = t.most_common(1)[0]
        else:
            target, _ = b.most_common(1)[0]
            from_top = False

        if t[target] + b[target] < len(tops):
            return -1

        count = 0
        if from_top:
            for i in range(len(tops)):
                if tops[i] != target:
                    if bottoms[i] != target:
                        continue
                    else:
                        tops[i] = bottoms[i]
                        count += 1

        else:
            for i in range(len(bottoms)):
                if bottoms[i] != target:
                    if tops[i] != target:
                        continue
                    else:
                        bottoms[i] = tops[i]
                        count += 1

        if len(set(tops)) == 1 or len(set(bottoms)) == 1:
            print(count)
            return count

        return -1

tops = [2,1,2,4,2,2]
bottoms = [5,2,6,2,3,2]
Solution().minDominoRotations(tops, bottoms)

tops = [3,5,1,2,3]
bottoms = [3,6,3,3,4]
assert -1 == Solution().minDominoRotations(tops, bottoms)

tops = [1,2,1,1,1,2,2,2]
bottoms = [2,1,2,2,2,2,2,2]
assert 1 == Solution().minDominoRotations(tops, bottoms)