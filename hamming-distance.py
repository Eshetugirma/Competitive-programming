class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        bitx =  ("0")*(33-len(bin(x))) + bin(x)[2:]
        bity = ("0")*(33-len(bin(y))) + bin(y)[2:]
        count = 0
        for i in range(max(len(bity),len(bitx))):
            count += int(bitx[i])^int(bity[i])
        return count