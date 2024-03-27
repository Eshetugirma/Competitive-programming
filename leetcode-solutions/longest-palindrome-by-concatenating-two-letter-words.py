class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        seen = defaultdict(int)
        maxLength = 0
        for c1,c2 in words:
            if seen[(c1,c2)]:
                seen[(c1,c2)] -= 1
                maxLength += 4
            else:
                seen[(c2,c1)] += 1
        for (c1,c2) in seen:
            if seen[(c1,c2)] and c1 == c2:
                maxLength += 2
                break
        return maxLength
        