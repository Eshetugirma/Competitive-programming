class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        seen = set(nums)
        mx = -1
        for num in nums:
            if -1*num in seen:
                mx = max(mx,abs(num))
        return mx
        