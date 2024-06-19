class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = reversed(s.split(' '))
        for word in arr:
            if word:
                return len(word)