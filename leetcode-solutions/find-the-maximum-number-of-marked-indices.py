class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        stack = []
        nums.sort()
        n = len(nums)
        
        count = 0
        for i in range(n):
            stack.append(2*nums[i])
        left,right = 0, n//2 + n%2 
        end = n//2 + n%2
        while right < n:
            if stack[left] <= nums[right]:
                print(left,right)
                count += 1
                left += 1
                right += 1
            else:
                right += 1
        # print(stack)
        # print(n)
        return count*2
