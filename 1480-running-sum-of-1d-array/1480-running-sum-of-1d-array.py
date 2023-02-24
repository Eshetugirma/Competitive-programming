class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        summ = 0
        #==>>> itarate every element and add to prefixsum with out offset
        for i in range(len(nums)):
            summ += nums[i]
            ans.append(summ)
        return ans