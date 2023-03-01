class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n<0:
            n=abs(n)
            x=1/x
        if n%2==0:
            temp = self.myPow(x,n//2)
            return temp*temp
        else:
            return self.myPow(x, n-1)*x
        
        
        