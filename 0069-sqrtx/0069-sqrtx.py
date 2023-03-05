class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        mid = 0
        if x == 1:
            return 1
        while left < right:
            mid = (left+right)//2
            if mid*mid == x or mid*mid < x < (mid+1)*(mid+1):
                return mid
            if mid * mid > x:
                right = mid
            else :
                left = mid+1
        return mid