class Solution:
    def addDigits(self, num: int) -> int:

        return num%9 if (num%9 or not num) else 9
        