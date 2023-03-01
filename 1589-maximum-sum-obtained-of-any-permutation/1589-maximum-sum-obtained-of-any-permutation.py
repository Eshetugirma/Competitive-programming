class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        #==>> dffine offset add requests at start and remove after end 
        offset = [0]*(len(nums))
        for start,end in requests:
            offset[start] += 1
            if end + 1 < len(nums):
                offset[end+1] -= 1
        #==>> take prefix sum of offset 
        pref = [0]
        for i in range(len(offset)):
            pref.append(pref[-1]+offset[i])
            
        nums.sort(reverse=True)
        pref.sort(reverse=True)
        ans = 0  
        
        
        for i in range(len(nums)):
            ans += nums[i]*pref[i]
        return ans%(10**9+7)
        