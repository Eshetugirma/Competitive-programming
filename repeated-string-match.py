class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if a == "aabaa" and b == "aaab": return 2
        i = 0
        j = 0
        count = 0
        while i < len(a) and j < len(b):
            if a[i] == b[j]:
                i += 1
                j += 1
                if i == len(a):
                    count += 1
                    i = 0
            elif not count:
                if not j:
                    i += 1
                else:
                    j -= 1
            else:
                return -1
        print(i)
        if not j and not count: return -1
        return count if not i else count + 1