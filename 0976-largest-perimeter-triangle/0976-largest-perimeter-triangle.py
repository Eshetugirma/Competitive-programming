class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        # iterate over n-3 to 0
        for i in range(len(nums)-3,-1,-1):
            if nums[i] + nums[i+1] > nums[i+2]: #checking if it is triangle 
                return nums[i] + nums[i+1] + nums[i+2]
        return 0