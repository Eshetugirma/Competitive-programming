class Solution:
    def minPartitions(self, n: str) -> int:
        max_possible = 0
        for num in n:
            max_possible = max(max_possible,int(num))
        return max_possible
        