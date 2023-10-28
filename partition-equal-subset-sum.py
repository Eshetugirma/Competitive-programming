class Solution:
    def canPartition(self, A: List[int]) -> bool:
        total_load = sum(A)
        n = len(A)
        dp = [[False] * (total_load + 1) for _ in range(n + 1)]
        
        # Initialize the first column of the dynamic programming table
        for i in range(n + 1):
            dp[i][0] = True
        
        # Fill the dynamic programming table
        for i in range(1, n + 1):
            for j in range(1, total_load + 1):
                dp[i][j] = dp[i - 1][j]
                if A[i - 1] <= j:
                    dp[i][j] |= dp[i - 1][j - A[i - 1]]
        
        min_diff = float('inf')
        for j in range(total_load // 2, -1, -1):
            if dp[n][j]:
                min_diff = total_load - 2 * j
                break
        
        return not min_diff