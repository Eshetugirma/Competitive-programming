class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap = defaultdict(int)
        left = 0
        max_length = 0
        for i in range(len(s)):
            hashmap[s[i]] += 1
            while hashmap[s[i]] > 1:
                hashmap[s[left]] -= 1
                if not hashmap[s[left]]:
                    del hashmap[s[left]]
                left += 1
            max_length = max(max_length,i-left+1)
        return max_length
                

