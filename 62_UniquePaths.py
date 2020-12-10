# my solution
# Time took: 40 min
# Time complexity: O(mn)
# Space complexity: O(mn)
import numpy as np

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def findPaths(m,n):
            # print("find path: %d, %d"%(m,n))
            if m < 0 or n < 0: return 0
            if m == 0 or n == 0: return 1    
            return -1

        if m == 1 and n == 1: return 1
    
        matrix = np.zeros((m,n))
        print("m=%d, n=%d"%(m,n))
        for i in range(0,n):
            for j in range(0,m):
                # print(j,i)
                print("find path: %d, %d"%(j,i))
                matrix[j][i] = max(matrix[j-1][i], findPaths(j-1,i)) + max(matrix[j][i-1], findPaths(j,i-1))
                print(matrix)
        return int(matrix[m-1][n-1])

#########################
# Solutions by LeetCode #
#########################

# Approach 1: Dynamic Programming
# Time complexity: O(mn)
# Space complexity: O(mn)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        d = [[1] * n for _ in range(m)]

        for col in range(1, m):
            for row in range(1, n):
                d[col][row] = d[col - 1][row] + d[col][row - 1]

        return d[m - 1][n - 1]

# Approach 2: Math (Python3 only)
# Time complexity: O((m+n)log(m+n)log(log(m+n))^2)
# Space complexity: O(1)
from math import factorial
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return factorial(m + n - 2) // factorial(n - 1) // factorial(m - 1)