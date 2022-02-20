'''
Level: Medium  Tag: [Union Find]

Given a list of accounts where each element accounts[i] is a list of strings,

where the first element accounts[i][0] is a name,

and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts.

Two accounts definitely belong to the same person if there is some common email to both accounts.

Note that even if two accounts have the same name,

they may belong to different people as people could have the same name.

A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts,

return the accounts in the following format: the first element of each account is the name,

and the rest of the elements are emails in sorted order.

The accounts themselves can be returned in any order.



Example 1:

Input: accounts = [
    ["John","johnsmith@mail.com","john_newyork@mail.com"],
    ["John","johnsmith@mail.com","john00@mail.com"],
    ["Mary","mary@mail.com"],
    ["John","johnnybravo@mail.com"]]
Output: [
    ["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],
    ["Mary","mary@mail.com"],
    ["John","johnnybravo@mail.com"]]
Explanation:
The first and second John's are the same person as they have the common email "johnsmith@mail.com".
The third John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer
[['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'],
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.

Example 2:

Input: accounts = [
    ["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],
    ["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],
    ["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],
    ["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],
    ["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
Output: [
    ["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],
    ["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],
    ["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],
    ["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],
    ["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]


Constraints:

1 <= accounts.length <= 1000
2 <= accounts[i].length <= 10
1 <= accounts[i][j] <= 30
accounts[i][0] consists of English letters.
accounts[i][j] (for j > 0) is a valid email.


'''

'''
初始化：每一个点都是一个集合，因此自己的父节点就是自己root[i]=i
查询：每一个节点不断寻找自己的父节点，若此时自己的父节点就是自己，那么该点为集合的根结点，返回该点。
修改：合并两个集合只需要合并两个集合的根结点，即fa[RootA]=RootB，其中RootA,RootB是两个元素的根结点

1.这道题可以抽象化为图中找connecting component的问题， 首先，将输入的email都看成图中的一个点
由于用户的姓名可以重复， 我们用owner来代表一个用户

2. 如何判断两个点是存在于同一个联通块中？同一个email的被不同的owner同时拥有，
那么这两个点(email)属于一个联通块。因此，需要构建owner的HashMap,
key-value pair的结构为：email : 拥有这个email的user的name
对属于同一个email[0]的email进行union操作，他们拥有至少一个共同的email, 判定他们是同一个用户，属于同一个联通块

3. 每一個email都有自己的root 確定每個email個共同root後
帶入owner找出對應的user name 並寫入list 即為所求

Time complixity O(n)啟用路徑壓縮可以到O(1)
Space complixity O(n) n為email數目
'''


class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        root = {}
        owner = {}
        def find(x):
            if root[x] == x:
                return x

            while root[x] != x:
                x = root[x]

            return x

        def union(a, b):
            root_a = find(a)
            root_b = find(b)

            if root_a != root_b:
                root[root_a] = root_b

        for acc in accounts:
            name = acc[0]
            emails = acc[1:]
            for i in range(len(emails)):
                if emails[i] not in root:
                    root[emails[i]] = emails[i]
                union(emails[0], emails[i])
                owner[emails[i]] = name

        group = defaultdict(set)
        for acc in accounts:
            emails = acc[1:]
            for email in emails:
                father = find(email)
                group[father].add(email)


        ans = []
        for k, v in group.items():
            ans.append([owner[k]] + sorted(list(v)))


        return ans


# accounts = [
#     ["John","johnsmith@mail.com","john_newyork@mail.com"],
#     ["John","johnsmith@mail.com","john00@mail.com"],
#     ["Mary","mary@mail.com"],
#     ["John","johnnybravo@mail.com"]]
# Solution().accountsMerge(accounts)


accounts = [
    ["David","David0@m.co","David4@m.co","David3@m.co"],
    ["David","David5@m.co","David5@m.co","David0@m.co"],
    ["David","David1@m.co","David4@m.co","David0@m.co"],
    ["David","David0@m.co","David1@m.co","David3@m.co"],
    ["David","David4@m.co","David1@m.co","David3@m.co"]]
Solution().accountsMerge(accounts)