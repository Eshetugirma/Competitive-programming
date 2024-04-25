class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        n = len(s)
    
        dp = [0]*(27+2*k)

        for c in s:
            index = ord(c) - 97 + k
            dp[index] = max(dp[index-k:index+k+1])+1
  
        return max(dp)
        