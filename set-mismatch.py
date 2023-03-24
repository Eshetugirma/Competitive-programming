class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        #===>> in-place element in nums to their correct position 
        while i < len(nums):
            if nums[nums[i]-1] != nums[i] and nums[i] != i+1:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
            else:
                i += 1
        #==>>> if there is number that is not at its correct position then it is duplecate
        for i in range(len(nums)):
            if nums[i] != i+1:
                return [nums[i],i+1]