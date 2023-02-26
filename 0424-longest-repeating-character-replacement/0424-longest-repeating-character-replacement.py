class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = defaultdict(int)
        max_len = 0
        left = 0
        #==>> add to your window dictionory as you can 
        for right in range(len(s)):
            window[s[right]] += 1
            #==>>> if difference b/n lenght of window and max val of window is greater than max opperation k then reduce window
            while (right-left+1) - max(window.values()) > k:
                window[s[left]] -= 1
                left += 1
            max_len = max(max_len,right-left+1)
        return max_len
                