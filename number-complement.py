class Solution:
    def findComplement(self, num: int) -> int:
        arr = ""
        ans = 0
        while num != 0:
            if num%2:
                arr += "0"
            else:
                arr += "1"
            num //= 2
        for i in range(len(arr)):
            ans += (2**i)*int(arr[i])
        return ans