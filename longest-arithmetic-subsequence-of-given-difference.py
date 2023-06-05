class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        memo = {}
        for i in range(len(arr)):
            if arr[i] - difference in memo:
                memo[arr[i]] = memo[arr[i]-difference] + 1
            else:
                memo[arr[i]] = 1
        return max(memo.values())