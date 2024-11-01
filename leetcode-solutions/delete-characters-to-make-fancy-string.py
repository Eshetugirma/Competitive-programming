class Solution:
    def makeFancyString(self, s: str) -> str:

        fancy = []

        count = 1

        for c in s:
            if fancy and fancy[-1] == c:
                count += 1
            else:
                count = 1
            if count < 3:
                fancy.append(c)

        return ''.join(fancy)
        