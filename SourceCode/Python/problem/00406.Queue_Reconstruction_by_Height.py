'''


Suppose you have a random list of people standing in a queue.

Each person is described by a pair of integers (h, k),

where h is the height of the person

and k is the number of people in front of this person who have a height greater than or equal to h.

Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.


Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]


'''


class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        def Mycmp(p1, p2):
            if p1[0] == p2[0]:
                return cmp(p2[1], p1[1])
            else:
                return cmp(p1[0], p2[0])

        if people == []:
            return []

        people.sort(cmp=Mycmp ,reverse=True)

        for i in xrange(len(people)):
            if people[i][1] != i:
                tmp = people.pop(i)
                people.insert(tmp[1], tmp)
        return people


Input = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
print Solution().reconstructQueue(Input)