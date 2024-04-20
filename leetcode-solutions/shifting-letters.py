class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        preSum = [0]
        total = sum(shifts)
        for i in range(len(s)):
            preSum.append(preSum[-1]+shifts[i])

        ans = []
        for i in range(len(s)):
            shift = (total - preSum[i])
            char = ((ord(s[i]) - 97) + shift)%26 + 97
            # print(char)
            ans.append(chr(char))

        return ''.join(ans)
        