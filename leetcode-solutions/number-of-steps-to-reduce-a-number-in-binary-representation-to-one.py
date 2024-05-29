class Solution:
    def numSteps(self, s: str) -> int:
        num =  int(s,2)
        count = 0
        # print(num)
        while num > 1:
            if num%2:
                num += 1
            else:
                num //= 2
            count += 1
        return count