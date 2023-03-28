class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        if  nums[0] > 1 or nums[-1] < 1:
            return 1
        elif len(nums) == 1:
            return 2 
        for i in range(len(nums)-1):
            if nums[i] <= 0 and nums[i+1]  > 1:
                return 1
            if nums[i] <= 0:
                continue
            if nums[i]+1 != nums[i+1]:
                return (nums[i] + 1)
        return nums[-1]+1