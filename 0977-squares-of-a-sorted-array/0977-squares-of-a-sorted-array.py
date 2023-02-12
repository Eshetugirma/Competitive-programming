class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        pointer = 0 
        while pointer < len(nums):
            nums[pointer] = nums[pointer]**2
            pointer += 1
        nums.sort()
        return nums