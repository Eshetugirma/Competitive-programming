class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = str(n)
        sums = 0
        product = 1
        #===>>> change the given int to str and itetate then find product and sum
        for i in s:
            product *= int(i)
            sums  += int(i)
        return product - sums