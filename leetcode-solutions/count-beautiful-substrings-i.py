class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowels = ['a','e','o','u','i']

        count = 0
        for i in range(len(s)):
            cons = 0 
            vowel = 0
            for j in range(i,len(s)):
            
                cons += (s[j] in vowels)
                
                vowel += (s[j] not in vowels)
                # print(vowel,cons)
                if cons == vowel and not (cons*vowel)%k:
                    count += 1
        return count
            
        