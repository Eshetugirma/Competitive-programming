class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        #==>> this is striaght forward binary search problem
        while left < right:
            mid = (left+right)//2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return right