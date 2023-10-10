class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        curr = nums[0]
        for i in range(1,len(nums)):
            curr &= nums[i]
        # if array AND can't be zero we consider all as one subarray
        if curr : return 1

        # if possible try to find subarrays separatly 
        count,start,curr = 0,0,nums[0]
        while start < len(nums) : 
            curr &= nums[start]
            if not curr :
                count += 1
                if start+1 < len(nums):
                    curr = nums[start+1]
            start += 1
                        
        return count