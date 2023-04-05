class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #===>>>> take offset for the case of negative number 
        if min(nums) < 0:
            offset = (min(nums))*-1
        else:
            offset = 0
        #===>>> add offset to every element 
        for i in range(len(nums)):
            nums[i] += offset
        ans = 0
        #==>>> shift all element nums 32 times
        for i in range(32):
            count = 0
            #===>>> count number of ones at the same index
            for num in nums:
                if (1 << i) & num:
                    count += 1
            #==>>> if there is reminder of our count then add value at that point to ans
            if count%3:
                ans += 2**(i)
        return ans - offset