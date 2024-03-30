class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        s = list(map(str,s.split(' ')))
        # print(s)
        curr = -1
        for c in s:
            if c.isdigit():
                if curr < int(c):
                    curr = int(c)
                else: return False
        return True

        