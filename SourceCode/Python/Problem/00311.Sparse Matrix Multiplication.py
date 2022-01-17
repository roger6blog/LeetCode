'''
Level: Medium   Tag: Matrix

Given two Sparse Matrix A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example1

Input:
[[1,0,0],[-1,0,3]]
[[7,0,0],[0,0,0],[0,0,1]]
Output:
[[7,0,0],[-7,0,3]]
Explanation:
A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]


     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |


Example2

Input:
[[1,0],[0,1]]
[[0,1],[1,0]]
Output:
[[0,1],[1,0]]


'''

class Solution:
    """
    @param A: a sparse matrix
    @param B: a sparse matrix
    @return: the result of A * B
    """
    def multiply(self, A, B):
        if not A or not B:
            return []


        row_a = len(A)
        row_b = len(B)
        col_a = len(A[0])
        col_b = len(B[0])

        new_matrix = [[0 for _ in range(col_b)] for _ in range(row_a)]
        for i in range(row_a):
            for j in range(col_b):
                for k in range(col_a):
                    new_matrix[i][j] += A[i][k] * B[k][j]


        print(new_matrix)

        return new_matrix



    def multiply_set(self, A, B):
        if not A or not B:
            return []


        row_a = len(A)
        row_b = len(B)
        col_a = len(A[0])
        col_b = len(B[0])
        non_zero_a = []
        non_zero_b = []

        new_matrix = [[0 for _ in range(col_b)] for _ in range(row_a)]
        for i in range(row_a):
            non_zero_a.append(set())
            for j in range(col_a):
                if A[i][j] != 0:
                    non_zero_a[i].add(j)


        for i in range(row_b):
            non_zero_b.append(set())
            for j in range(col_b):
                if B[i][j] != 0:
                    non_zero_b[i].add(j)

        for i in range(row_a):
            mark_a = non_zero_a[i]
            for j in range(col_b):
                mark_b = non_zero_b[j]
                for k in mark_a & mark_b:
                    new_matrix[i][j] = A[i][k] * B[k][j]


        print(new_matrix)

        return new_matrix

a = [[1,0,0],[-1,0,3]]
b = [[7,0,0],[0,0,0],[0,0,1]]
Solution().multiply(a, b)
Solution().multiply_set(a, b)