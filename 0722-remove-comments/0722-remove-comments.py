class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        s = '\n'.join(source) + '\n' 
        i = 0
        res = ''
        while i < len(s):
            if i + 1 < len(s) and s[i] == s[i+1] == '/':
                idx = s.find('\n', i+2)
                i = idx
            elif i + 1 < len(s) and s[i] == '/' and s[i+1] == '*':
                idx = s.find('*/', i+2)
                i = idx + 2
            else:
                res += s[i]
                i += 1
        arr = res.split('\n')
        return filter(len, arr)