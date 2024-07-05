class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = defaultdict(int)
        left,ans = 0, 0
        for right in range(len(s)):
            window[s[right]] += 1
            while len(window) < (right-left+1):
                window[s[left]] -= 1
                
                if not window[s[left]]: 
                    del window[s[left]]
                left += 1
            ans = max(ans,right-left+1)
        return ans