class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        given = x
        reverted_number = 0
        while x:
            reverted_number = reverted_number*10 + x % 10
            x //= 10
        return reverted_number == given
        