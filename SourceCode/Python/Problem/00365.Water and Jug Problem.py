'''
Level: Medium

You are given two jugs with capacities jug1Capacity and jug2Capacity liters.

There is an infinite amount of water supply available.

Determine whether it is possible to measure exactly targetCapacity liters using these two jugs.

If targetCapacity liters of water are measurable,

you must have targetCapacity liters of water contained within one or both buckets by the end.

Operations allowed:

Fill any of the jugs with water.
Empty any of the jugs.
Pour water from one jug into another till the other jug is completely full,
or the first jug itself is empty.


Example 1:

Input: jug1Capacity = 3, jug2Capacity = 5, targetCapacity = 4
Output: true
Explanation: The famous Die Hard example
Die hard 3 : Jugs Problem
https://www.youtube.com/watch?v=BVtQNK_ZUJg

Example 2:

Input: jug1Capacity = 2, jug2Capacity = 6, targetCapacity = 5
Output: false
Example 3:

Input: jug1Capacity = 1, jug2Capacity = 2, targetCapacity = 3
Output: true

Constraints:

1 <= jug1Capacity, jug2Capacity, targetCapacity <= 10^6

'''




'''
这道问题其实可以转换为有一个很大的容器，我们有两个杯子，容量分别为x和y，问我们通过用两个杯子往里倒水，和往出舀水，
问能不能使容器中的水刚好为z升。那么我们可以用一个公式来表达:

z = m * x + n * y

其中m，n为舀水和倒水的次数，正数表示往里舀水，负数表示往外倒水，那么题目中的例子可以写成:
4 = (-2) * 3 + 2 * 5
即3升的水罐往外倒了两次水，5升水罐往里舀了两次水。
那么问题就变成了对于任意给定的x,y,z，存不存在m和n使得上面的等式成立。

根据裴蜀定理，ax + by = d的解为 d = gcd(x, y)，那么我们只要只要z % d == 0，上面的等式就有解，所以问题就迎刃而解了，
我们只要看z是不是x和y的最大公因数的倍数就行了，
别忘了还有个限制条件x + y >= z，因为x和y不可能称出比它们之和还多的水

'''




class Solution(object):
    def canMeasureWater(self, jug1Capacity, jug2Capacity, targetCapacity):
        """
        :type jug1Capacity: int
        :type jug2Capacity: int
        :type targetCapacity: int
        :rtype: bool
        """
        from fractions import gcd

        x = jug1Capacity
        y = jug2Capacity

        if x + y < targetCapacity:
            return False

        n = gcd(x, y)
        if targetCapacity % n == 0:
            return True

        return False


jug1Capacity = 3
jug2Capacity = 5
targetCapacity = 4
assert True == Solution().canMeasureWater(jug1Capacity, jug2Capacity, targetCapacity)

jug1Capacity = 2
jug2Capacity = 6
targetCapacity = 5
assert False == Solution().canMeasureWater(jug1Capacity, jug2Capacity, targetCapacity)

jug1Capacity = 1
jug2Capacity = 2
targetCapacity = 3
assert True == Solution().canMeasureWater(jug1Capacity, jug2Capacity, targetCapacity)

jug1Capacity = 34
jug2Capacity = 5
targetCapacity = 6
assert True == Solution().canMeasureWater(jug1Capacity, jug2Capacity, targetCapacity)

jug1Capacity = 1
jug2Capacity = 1
targetCapacity = 12
assert False == Solution().canMeasureWater(jug1Capacity, jug2Capacity, targetCapacity)