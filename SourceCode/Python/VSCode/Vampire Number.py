'''
Google Interview problem

Vampire number:
positive integer v that can be factored into two integers x*y,
where base-10 digits of v are equal to the set of base-10 digits of x and y.
These two factors are called the fangs.
Examples:
688 = 86 x 8
1260 = 21 x 60
1530 = 30 x 51
125460 = 204 x 615 = 246 x 510
12546 = 246 x 51

Please implement a method to check if it is a vampire number.

'''

class Solution(object):
    def isVampreNumber(self, num):
        """
        :type num: int
        :rtype: bool
        pass
        """
        str_num = str(num)
        from itertools import permutations

        for p in permutations(str_num):
            v = ''.join(p)
            x, y = v[:int(len(v)/2)], v[int(len(v)/2):]
            if int(x) * int(y) == num:
                return True
        pass




num = 688
assert True == Solution().isVampreNumber(num)
num = 125460
assert True == Solution().isVampreNumber(num)