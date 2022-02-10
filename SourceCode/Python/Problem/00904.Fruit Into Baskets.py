'''
Level: Medium

You are visiting a farm that has a single row of fruit trees arranged from left to right.

The trees are represented by an integer array fruits where
fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible.
However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit.
There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree
(including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.


Example 1:

Input: fruits = [1,2,1]
Output: 3
Explanation: We can pick from all 3 trees.

Example 2:

Input: fruits = [0,1,2,2]
Output: 3
Explanation: We can pick from trees [1,2,2].
If we had started at the first tree, we would only pick from trees [0,1].

Example 3:

Input: fruits = [1,2,3,2,2]
Output: 4
Explanation: We can pick from trees [2,3,2,2].
If we had started at the first tree, we would only pick from trees [1,2].


Constraints:

1 <= fruits.length <= 10^5
0 <= fruits[i] < fruits.length


'''

class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        from collections import deque, Counter
        if len(fruits) <= 2 or len(Counter(fruits)) <= 2:
            return len(fruits)

        queue = deque()
        ans = 0
        for f in fruits:
            queue.append(f)
            c = Counter(queue)
            while len(c) > 2:
                queue.popleft()
                c = Counter(queue)

            ans = max(ans, len(queue))

        print(ans)

        return ans

fruits = [1,2,3,2,2]
Solution().totalFruit(fruits)

fruits = [0,1,2,2]
Solution().totalFruit(fruits)

fruits = [3,3,3,1,2,1,1,2,3,3,4]
assert 5 == Solution().totalFruit(fruits)

fruits = [3,3,3,3,3,3]
assert 6 == Solution().totalFruit(fruits)