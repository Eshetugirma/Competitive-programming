class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0 
        for num in nums:
            count += bool(num%3)
        return count
                
