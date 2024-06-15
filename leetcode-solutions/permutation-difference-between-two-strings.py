class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        memo = defaultdict(int)
        for i in range(len(s)):
            memo[s[i]] = i
        count = 0
        for i in range(len(s)):
            count += abs(i-memo[t[i]])
        return count