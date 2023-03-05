class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        num = nums + nums
        stack = []
        #==>>> create num which contain double of nums as circled 
        for i in range(len(nums)):
            stack.append(nums[i])
            for j in range(i,len(num)):
                if stack[i] < num[j]:
                    stack[i] = num[j]
                    break
            if stack[i] == num[i]:
                stack[i] = -1
        return stack
                 