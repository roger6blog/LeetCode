'''
Suppose you are at a party with n people (labeled from 0 to n - 1) and among them,
there may exist one celebrity.
The definition of a celebrity is that all the other n - 1 people know him/her
but he/she does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one.
The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?"
to get information of whether A knows B.
You need to find out the celebrity (or verify there is not one) by asking as few questions as possible
(in the asymptotic sense).

You are given a helper function bool knows(a, b)which tells you whether A knows B.
Implement a function int findCelebrity(n).
There will be exactly one celebrity if he/she is in the party.
Return the celebrity's label if there is a celebrity in the party.
If there is no celebrity, return -1.


Example:

"../../../227.Example-1.png"

Input: graph = [[1,1,0],[0,1,0],[1,1,1]]
Output: 1
Explanation: There are three persons labeled with 0, 1 and 2.
graph[i][j] = 1 means person i knows person j,
otherwise graph[i][j] = 0 means person i does not know person j.
The celebrity is the person labeled as 1 because both 0 and 2 know him but 1 does not know anybody.


Exmaple2:

"../../../227.Example-2.png"

Input: graph = [[1,0,1],[1,1,0],[0,1,1]]
Output: -1
Explanation: There is no celebrity.

Constraints:
n == graph.length
n == graph[i].length
2 <= n <= 100
graph[i][j] is 0 or 1.
graph[i][i] == 1
Follow up: If the maximum number of allowed calls to the API knows is 3 * n, c
ould you find a solution without exceeding the maximum number of calls?

'''

class Solution:
    # @param {int} n a party with n people
    # @return {int} the celebrity's label or -1

    def findCelebrity(self, n):
        # 首先假設第一個人是名人(用head 表示現在誰有可能是名人)
        head = 0
        for i in range(1, n):
            # 如果head 不知道下一個人是誰，下一個人就一定不是名人，head 保持不變
            if not Celebrity.knows(head, i):
                continue
            # 如果 head 知道下一個人是誰，就代表 head 一定不是名人，所以現在第 i 個人有可能是
            else:
                head = i
        # 還必須要大家都認識他，因此循環一次
        for i in range(n):
            if not Celebrity.knows(i, head):
                head = -1
                break
        # head 還有可能知道他前面的人是誰。因此還需要跑一次迴圈
        for i in range(0, head):
            if Celebrity.knows(head, i):
                head = -1
                break
        return head