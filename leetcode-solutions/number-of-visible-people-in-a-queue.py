class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        stack = []
        ans = [0]*len(heights) 
        for i in range(len(heights)):
            while stack and heights[stack[-1]] <= heights[i]:
                pop = stack.pop()
                ans[pop] += 1
            if stack:
                ans[stack[-1]] += 1
            stack.append(i)
        return ans

