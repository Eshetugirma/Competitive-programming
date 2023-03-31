class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bit = bin(n)
        for i in range(2,len(bit)-1):
            if bit[i] == bit[i+1]:
                return False
        return True