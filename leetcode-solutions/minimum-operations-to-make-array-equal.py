class Solution:
    def minOperations(self, n: int) -> int:
        stack = []
        for i in range(n):
            stack.append(2*i+1)
        left, right,ans = 0, n-1,0
        while left < right:
            ans += (stack[left]+stack[right])//2 - stack[left]
            left += 1
            right -= 1
        return ans            
        