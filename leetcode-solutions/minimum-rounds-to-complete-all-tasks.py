class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        count = Counter(tasks)
        if min(count.values()) == 1: return -1
        ans = 0
        for val in count.values():
            ans += val//3 + bool(val%3)
        return ans
        