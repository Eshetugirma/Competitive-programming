class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        mid = nums[n//2]
        total = 0
        for i in range(n):
            total += abs(nums[i]-mid)
        return total