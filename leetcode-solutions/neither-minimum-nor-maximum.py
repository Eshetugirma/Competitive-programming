class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        mn = min(nums)
        mx = max(nums)
        for num in nums:
            if num != mx and num != mn:
                return num
        return -1