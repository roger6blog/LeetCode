'''
Level: Medium

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

Explanation:
Person 0 has height 5 with no other people taller or the same height in front.
Person 1 has height 7 with no other people taller or the same height in front.
Person 2 has height 5 with two persons taller or the same height in front, which is person 0 and 1.
Person 3 has height 6 with one person taller or the same height in front, which is person 1.
Person 4 has height 4 with four people taller or the same height in front, which are people 0, 1, 2, and 3.
Person 5 has height 7 with one person taller or the same height in front, which is person 1.
Hence [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] is the reconstructed queue.


Example 2:

Input: people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
Output: [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]


Constraints:

1 <= people.length <= 2000
0 <= hi <= 10^6
0 <= ki < people.length
It is guaranteed that the queue can be reconstructed.

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