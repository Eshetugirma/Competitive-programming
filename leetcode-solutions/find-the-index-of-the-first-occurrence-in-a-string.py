class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        target,window = 0,0
        t = len(needle)
        n = len(haystack)
        if t > n: return -1
        # print(ord("a"))
        for i in range(t):
            target += (ord(needle[i])-97)*(26**(t-1-i))
            window += (ord(haystack[i])-97)*(26**(t-1-i))
            target = target%(10**9+7)
            window = window%(10**9+7)
        if window == target: return 0
        for right in range(t,n):
            window -= (ord(haystack[(right-t)])-97)*(26**(t-1))
            window *= 26
            window += (ord(haystack[right])-97)
            window = window%(10**9+7)
            # print(haystack[right-t], haystack[right], window, target)
            
            if target == window: return right - t + 1
        return -1
            

        