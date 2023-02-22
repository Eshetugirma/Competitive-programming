class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        maxx = 0
        left = 0 
        right = 0
        #===>>>>  iterate and see if the element is reapeted
        while right<len(s):
            #===>>> if the element is reapeted then remove s[left] move left
            if s[right] in window:
                window.remove(s[left])
                left += 1
            #==>>>>> if not reapeted add s[right] then move right and update max
            else:
                window.add(s[right])
                maxx = max(maxx,len(window))
                right += 1
        return maxx
                
                