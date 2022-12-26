class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        my_count = 0
        my_dict = {}
        
        for n in nums:
            # Check to see if number has already been encountered
            if n in my_dict:
                # Increase count by the number of previous instances
                my_count += my_dict[n]

                # Increase the count of previous observation
                my_dict[n] +=1
            else:
                # Store newly encountered number along with its count
                my_dict[n] = 1
                
        return my_count