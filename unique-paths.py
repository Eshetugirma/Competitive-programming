class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for i in range(m) ]
        dp[-1][-1] = 1
        def check(row,col):
            if 0 <= row < m and 0 <= col < n:
                return dp[row][col]
            return 0 
        for row in range(m-1,-1,-1):
            for col in range(n-1,-1,-1):
                dp[row][col] += check(row+1,col) + check(row,col+1)
        return dp[0][0]