class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        seen = Counter(arr)
        return len(seen.values()) == len(set(seen.values()))
        