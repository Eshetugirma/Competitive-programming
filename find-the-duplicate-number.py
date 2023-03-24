class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        i = 0
        #===>> in-place element in nums to their correct position 
        while i < len(nums):
            if nums[nums[i]-1] != nums[i] and nums[i] != i+1:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
            else:
                i += 1
        #===>>> there is only one number that is not at its position then return it
        for i in range(len(nums)):
            if nums[i] != i+1:
                return nums[i]