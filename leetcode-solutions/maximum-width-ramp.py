class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        
        n = len(nums)
        indices = [i for i in range(n)]
        indices.sort(key=lambda i:(nums[i], i))

        min_index  = n
        max_width_ramp = 0

        for i in indices:
            
            max_width_ramp = max(max_width_ramp, i - min_index)
            min_index = min(min_index,i)
            
        return max_width_ramp