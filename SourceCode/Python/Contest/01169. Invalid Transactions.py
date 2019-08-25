'''
1169. Invalid Transactions

Difficulty: Easy
A transaction is possibly invalid if:

the amount exceeds $1000, or;
if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.
Each transaction string transactions[i] consists of comma separated values representing the name, time (in minutes), amount, and city of the transaction.

Given a list of transactions, return a list of transactions that are possibly invalid.  You may return the answer in any order.



Example 1:

Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
Output: ["alice,20,800,mtv","alice,50,100,beijing"]
Explanation: The first transaction is invalid because the second transaction occurs within a difference of 60 minutes, have the same name and is in a different city. Similarly the second one is invalid too.
Example 2:

Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
Output: ["alice,50,1200,mtv"]
Example 3:

Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
Output: ["bob,50,1200,mtv"]


Constraints:

transactions.length <= 1000
Each transactions[i] takes the form "{name},{time},{amount},{city}"
Each {name} and {city} consist of lowercase English letters, and have lengths between 1 and 10.
Each {time} consist of digits, and represent an integer between 0 and 1000.
Each {amount} consist of digits, and represent an integer between 0 and 2000.


'''

class Solution(object):
    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        invalid_rec = []

        acc_name = {}
        for c, rec in enumerate(transactions):
            cols = rec.split(",")
            if int(cols[2]) > 1000:
                invalid_rec.append(transactions[c])
            if cols[0] not in acc_name:
                acc_name[cols[0]] = (cols[1], cols[3])
            else:
                if abs(int(cols[1]) - int(acc_name[cols[0]][0])) < 60 and cols[3] != acc_name[cols[0]][1]:
                    if transactions[c] not in invalid_rec:
                        invalid_rec.append(transactions[c])
                    if c != 0:
                        if transactions[c-1] not in invalid_rec:
                            invalid_rec.append(transactions[c-1])

        return invalid_rec


# transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
transactions = ["alex,676,260,bangkok","bob,656,1366,bangkok","alex,393,616,bangkok","bob,820,990,amsterdam","alex,596,1390,amsterdam"]
print(Solution().invalidTransactions(transactions))