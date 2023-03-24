class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.append(n+1)
        i = 0
        while i < len(nums):
            if nums[i] != i and nums[i] != n+1:
                nums[nums[i]],nums[i] = nums[i],nums[nums[i]]
            else:
                i += 1
        return nums.index(n+1)