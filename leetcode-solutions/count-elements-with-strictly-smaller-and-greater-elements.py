class Solution:
    def countElements(self, nums: List[int]) -> int:
        nums.sort()
        ans = len(nums) - nums.count(nums[0])- nums.count(nums[-1]) 
        return ans if ans >= 1 else 0