class Solution:
    def countOdds(self, low: int, high: int) -> int:
        #===>>> if both number are even then return half of their difference
        if low%2 == 0 and high%2 == 0:
            return (high-low)//2
        #====>>>> else return half plus one 
        else:
            return ((high-low)//2 +1)
            
            