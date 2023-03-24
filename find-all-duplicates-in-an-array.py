class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        i = 0
        while i < len(nums):
            #===>>>> this to in-place all number in list to their correct position
            if nums[i] != i + 1 and nums[i] != nums[nums[i]-1]:
                nums[nums[i]-1],nums[i] = nums[i],nums[nums[i]-1]
            else:
                i += 1
        res = []
        for i in range(len(nums)):
            if nums[i] != i+1:
                res.append(nums[i])
        return res