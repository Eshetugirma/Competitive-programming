class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        current = 0
        count = 0
        for num in nums:
            
            if count == 0:
                current = num
                
            count += current == num
            count -= current != num

        return current 

            

