class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            count = [0]*26
            
            for ch in s:
                count[ord(ch)-ord("a")] += 1
            ans[tuple(count)].append(s)
                
        return ans.values()
        