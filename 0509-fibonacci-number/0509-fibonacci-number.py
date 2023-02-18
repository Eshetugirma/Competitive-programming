class Solution:
    def fib(self, n: int) -> int:
        if n>1:
            #==>>> add last two value of function
            return self.fib(n-1) + self.fib(n-2)
        #==>> this is the base case value
        elif n==1:
            return 1
        else:
            return 0