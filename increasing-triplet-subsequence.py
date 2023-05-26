class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        mn1 = mn2 = float('inf')
        for i in range(len(nums)):
            if mn1 < mn2 < nums[i]:
                return True
            elif nums[i] < mn1:
                mn1 = nums[i]
            elif mn1 < nums[i] < mn2:
                mn2 = nums[i]
        return False