class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        for i in range(n,2*n+1):
            if i%2 == 0 and i%n == 0:
                break
        return i