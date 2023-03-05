class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack,ans = [],[-1]*len(nums)
        #==>> this is the optimal solution by monotonik stack 
        for ind in range(len(nums)*2):
            i = ind%len(nums)
            #==>> while stack and num at index of top stack is greater than at current index then update ans to nums at current index
            while stack and nums[stack[-1]] < nums[i]:
                ans[stack.pop()] = nums[i]
            stack.append(i)
        return ans