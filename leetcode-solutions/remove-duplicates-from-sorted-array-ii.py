class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        mx = max(nums) + 1 
        k = 0
        for i in range(2,len(nums)):
            if nums[i-1] == nums[i-2] == nums[i]:
                nums[i-2] = mx 
                k += 1
        
        left = 0 
        for right in range(len(nums)): 
            # print(nums[left],nums[right])
            if nums[right] != mx: 
                nums[left],nums[right] = nums[right],nums[left] 
                left += 1
        return len(nums) - k