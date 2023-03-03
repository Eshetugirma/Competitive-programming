class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        target = needle
        window = haystack[:len(needle)]
        #==>>> this is brute force solution for this problem
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(target)] == target:
                return i
        return -1