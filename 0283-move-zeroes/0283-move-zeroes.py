class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = 0
        while right < len(nums):
            if nums[left] == 0 and nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                right += 1
                left += 1
            elif nums[left] == 0 and nums[right] == 0:
                right += 1

            else:
                right += 1
                left += 1
        return nums