class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        window = 0
        const = power**(k)%modulo

        for i in range(len(s)-1,-1,-1):
            window = (window*power + (ord(s[i])-96))%modulo

            if i+k < len(s):
                window = (window - (ord(s[i+k])-96)*const)%modulo
            # window = window % modulo 
            # print(window,hashValue)
            if window%modulo == hashValue: ind = i
        return s[ind:ind+k]