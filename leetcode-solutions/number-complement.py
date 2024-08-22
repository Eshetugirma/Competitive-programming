class Solution:
    def findComplement(self, num: int) -> int:
        s = bin(num)[2:]
        arr = []
        for c in s:
            if c == '0':
                arr.append('1')
            else:
                arr.append('0')
        res = ''.join(arr)
        return int(res,2)

        