'''
Level: Medium   Tag: [Math]

Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

You must write an algorithm that runs in O(n) time and uses O(1) extra space.


Example 1:

Input: n = 13
Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]

Example 2:

Input: n = 2
Output: [1,2]


Constraints:

1 <= n <= 5 * 10^4


'''



'''
按个位数遍历，在遍历下一个个位数之前，先遍历十位数，十位数的高位为之前的个位数，只要这个多位数并没有超过n，就可以一直往后遍历
如果超过了，我们除以10，然后再加1，如果加1后末尾形成了很多0，那么我们要用个while循环把0都去掉，然后继续运算

'''


class Solution(object):
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def cmp(a, b):
            if str(a) > str(b):
                return 1
            return -1


        ans = [i for i in range(1, n+1)]
        ans.sort(cmp=cmp)
        print(ans)
        return ans


    def lexicalOrder2(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        curr = 1
        ans = []
        for _ in range(1, n+1):
            ans.append(curr)
            if curr * 10 <= n:
                curr *= 10
            elif curr % 10 != 9 and curr + 1 <= n:
                curr += 1
            else:
                while (curr//10) % 10 == 9:
                    curr //= 10
                curr = curr // 10 + 1

        print(ans)
        return ans

n = 13
Solution().lexicalOrder(n)
Solution().lexicalOrder2(n)