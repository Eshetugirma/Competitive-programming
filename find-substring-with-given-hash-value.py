class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        window = 0
        const = power**(k)%modulo
        # iterate backward so that we can ignore division by power which create problem
        for i in range(len(s)-1,-1,-1):
            window = (window*power + (ord(s[i])-96))%modulo

            # if window is above k decrease 
            if i+k < len(s):
                window = (window - (ord(s[i+k])-96)*const)%modulo

            # if we see valid window then update starting index 
            if window%modulo == hashValue: ind = i
        return s[ind:ind+k]