class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        checker = False
        prefix_sum = [0]
        #===>>> form the prefix sum of nums with off set 
        for i in range(len(nums)):
            prefix_sum.append(prefix_sum[i]+nums[i])
        #==>>>>  check if prefix_sum
        for i in range(len(prefix_sum)-1):
            half = (prefix_sum[-1]+prefix_sum[i]-prefix_sum[i+1])/2
            center = prefix_sum[-1]-prefix_sum[i+1]
            if center == half:
                checker = True
                break
        if not checker:
            return -1
        return i