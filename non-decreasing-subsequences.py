class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        def backtracking(index,temp,nums):        
            if len(temp) > 1:
                ans.add(tuple(temp))
            for i in range(index,len(nums)):
                if not temp or temp[-1] <= nums[i]:
                    backtracking(i+1,temp + [nums[i]],nums)
        backtracking(0,[],nums)
        return ans