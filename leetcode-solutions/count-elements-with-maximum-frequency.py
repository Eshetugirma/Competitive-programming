class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = Counter(nums)
        mx = max(counter.values())
        ans = 0
        for key, val in counter.items():
            print(counter,mx)
            if val == mx:
                ans += val
        return ans