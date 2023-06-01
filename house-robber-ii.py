class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        rob1,rob2 = 0,0
        for i in range(len(nums)-1):
            temp = max(rob1+nums[i],rob2)
            rob1 = rob2
            rob2 = temp
        ans = rob2
        rob1,rob2 = 0,0
        for i in range(1,len(nums)):
            temp = max(rob1+nums[i],rob2)
            rob1 = rob2
            rob2 = temp
        return max(ans,rob2)