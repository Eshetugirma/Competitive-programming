class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for left in range(len(nums)-1):
            mini = left
            for right in range(left+1,len(nums)):
                if nums[right] < nums[mini]:
                    mini = right
            if left != right:
                nums[left],nums[mini] = nums[mini],nums[left]