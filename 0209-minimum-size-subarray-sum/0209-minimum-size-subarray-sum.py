class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        summ = 0
        left = 0
        right = 0
        minimal = len(nums) + 1
        while right<(len(nums)):
            # print(summ)
            if summ < target:
                summ += nums[right]
                right += 1
            else:
                # print(right,left)
                minimal = min(minimal,right-left)
                summ -= nums[left]
                left += 1
        while summ >= target:
            minimal = min(minimal,right-left)
            summ -= nums[left]
            left += 1
        if minimal > len(nums):
            return 0
        return minimal