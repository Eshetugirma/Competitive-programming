class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        if len(set(s)) == 1: return n
        dp = [0]*n 
        # reversed_s = s[::-1]
        for i in range(n-1,-1,-1):
            # print(dp)
            new_dp = [0]*n
            new_dp[i] = 1
            for j in range(i+1,n):
                
                if s[i] == s[j]:
                    new_dp[j] = 2 + dp[j-1]
                else:
                    new_dp[j] = max(dp[j],new_dp[j-1])
                # print( 11111,new_dp)
            dp = new_dp
        return dp[-1]