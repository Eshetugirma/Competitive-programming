class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        s = str(num)
        for c in s:
            if not num%int(c):
                count += 1
        return count