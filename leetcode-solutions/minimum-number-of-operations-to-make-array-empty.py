class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = Counter(nums)
        if min(count.values()) < 2: return -1
        ans = 0
        for val in count.values():
            ans += val//3 + int(val%3 != 0)
        return ans