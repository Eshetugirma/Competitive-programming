class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        
        s = list(palindrome)
        n = len(s)
        if n <= 1:
            return ''

        for i in range(n):

            if s[i] != 'a' and (not n%2 or i != n//2) :
                s[i] = 'a'

                return ''.join(s)

        s[-1] = 'b'

        return ''.join(s)