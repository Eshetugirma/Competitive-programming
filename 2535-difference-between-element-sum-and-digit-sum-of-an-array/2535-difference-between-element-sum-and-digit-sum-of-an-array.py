class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        el_sum = sum(nums)#==>> sum all elements in nums
        dig_sum = 0
        #===>>> add each digits in nums separately
        for i in range(len(nums)):
            s = str(nums[i])
            for j in s:
                dig_sum += int(j)
        return abs(el_sum-dig_sum)