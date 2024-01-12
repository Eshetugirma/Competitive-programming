class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        count = 0
        half = 0
        seen = 'aeiouAEIOU'
        for i in range(len(s)):
            count += (s[i] in seen)
            if i < len(s)//2:
                half += (s[i] in seen)
        print(count,half)
        return not count%2 and (count - count//2) == half
        