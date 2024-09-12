class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        s = set(allowed)
        count = 0
        for word in words:
            for char in word:
                if char not in s:
                    count -= 1
                    break
            count += 1
        return count