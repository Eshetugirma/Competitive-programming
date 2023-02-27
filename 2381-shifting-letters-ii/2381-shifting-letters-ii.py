class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        offset = [0]*(n+1)
        #==>> create offset and do shifts operation on it 
        for start,end,direction in shifts:
            if direction == 1:
                offset[start] += 1
                offset[end+1] -= 1
            else:
                offset[start] -= 1
                offset[end+1] += 1
        #==>> prefix sum of offset complete shift operation 
        for i in range(1,n):
            offset[i] += offset[i-1]
        ans = []
        orde = ord('a')
        #==>> combine offset and s at ans list after return by joining to string
        for i,c in enumerate(s):
            curr = (ord(c) - orde + offset[i])%26
            ans.append(chr(curr+orde))
        return "".join(ans)