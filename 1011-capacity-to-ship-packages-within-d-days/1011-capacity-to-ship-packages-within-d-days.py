class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left,right = max(weights),sum(weights)
        
        while left < right:
            mid = (left + right)//2
            if_day = 1
            weight_per_day = 0
            
            
            for i in range(len(weights)):
                weight_per_day += weights[i]
                
                if weight_per_day > mid:
                    weight_per_day = weights[i]
                    if_day += 1
                    
                if if_day > days:
                    break
                    
            if if_day <= days:
                right = mid
                
            else:
                left = mid+1
        return right
            