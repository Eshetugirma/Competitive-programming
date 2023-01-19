class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        ans = nums
        for i in range(n):
            string = str(nums[i])
            reverse = string[::-1]
            ans.append(int(reverse))
        return len(set(ans))