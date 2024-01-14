class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        count1 = Counter(word1)
        count2 = Counter(word2)

        first,second = sorted(count1.values()),sorted(count2.values())
        return first == second and set(word1) == set(word2)