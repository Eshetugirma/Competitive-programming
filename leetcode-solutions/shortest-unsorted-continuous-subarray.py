class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        count = 0
        forward, backward = 1,1
        n = len(nums)-1
        sorted_nums = sorted(nums)
        if sorted_nums == nums: return 0
        for i in range(len(nums)):
            if nums[i] == sorted_nums[i] and forward:
                count += 1
            else:
                forward = 0
            if nums[n-i] == sorted_nums[n-i] and backward:
                count += 1
            else:
                backward = 0
        return n - count + 1
            
        