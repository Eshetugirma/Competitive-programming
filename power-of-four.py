class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        #==>>> recursivily check all multply of four unt
        if n>1:
            return self.isPowerOfFour(n/4)
        elif n==1:
            return True
        else:
            return False