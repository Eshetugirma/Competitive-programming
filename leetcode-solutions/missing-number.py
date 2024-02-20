class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)+1):
            nums.append(i)
        ans = 0
        for i in range(len(nums)):
            ans ^= nums[i]

        return ans
        