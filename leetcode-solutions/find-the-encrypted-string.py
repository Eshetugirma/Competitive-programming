class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        ans = []
        for i in range(len(s)):
            i = (i+k)%len(s)
            ans.append(s[i])
        return ''.join(ans)