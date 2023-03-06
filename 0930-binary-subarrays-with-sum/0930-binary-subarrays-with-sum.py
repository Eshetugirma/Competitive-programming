class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = defaultdict(int)
        pref = [0]
        #==>>> take prefix sum with offset 
        for num in nums:
            pref.append(num+pref[-1])
        ans = 0
        #==>> for every num in prefix sum add count of subarry you can form with current num
        for num in pref:
            ans += count[num-goal]
            count[num] += 1
        return ans
        
