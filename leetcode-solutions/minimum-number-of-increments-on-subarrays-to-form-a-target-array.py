class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        count = target[0]
        for i in range(1,len(target)):
            count += max(target[i]-target[i-1],0)
        return count
        