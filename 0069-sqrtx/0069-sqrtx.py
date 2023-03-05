class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        mid = 0
        #==>>> this is to handle the edge case at one 
        if x == 1:
            return 1
    
        while left < right:
            mid = (left+right)//2
            #==>> if see the sqrt return and break
            if mid*mid == x or mid*mid < x < (mid+1)*(mid+1):
                return mid
            
            #==>> if mid is greater than expected val then take to right else to left
            if mid * mid > x:
                right = mid
            else :
                left = mid+1
        return mid