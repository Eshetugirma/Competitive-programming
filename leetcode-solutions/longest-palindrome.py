class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        longest_palandrome = 0
        odd = 0
        for val in count.values():
            longest_palandrome += val - val%2
            if val%2: odd = 1
        return longest_palandrome + odd

        