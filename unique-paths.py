class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        fact = factorial(m-1)
        count = 1
        for i in range(n,m+n-1):
            count *= i
        return count//fact