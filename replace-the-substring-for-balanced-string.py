class Solution:
    def balancedString(self, s: str) -> int:
        count = Counter(s)
        balanced = len(s)//4
        ans = len(s)
        left = 0
        #==>> use sliding window once you pass then see element out side of window 
        for right in range(len(s)):

            count[s[right]] -= 1
            #==>> if the element in the window is all less than  balancing point out side is balanced 
            while left < len(s) and max(count.values()) <= balanced:
                ans = min(ans,right-left+1)
                count[s[left]] += 1
                left+=1
        return ans