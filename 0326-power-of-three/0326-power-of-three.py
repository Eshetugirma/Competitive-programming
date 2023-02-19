class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if abs(n)>1:
            return self.isPowerOfThree(n/3)
        elif n==1:
            return True
        else:
            return False
            