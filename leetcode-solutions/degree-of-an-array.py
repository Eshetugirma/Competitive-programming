class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = Counter(nums)
        mx = max(count.values())
        memo = nums[::-1]
        ans = inf
        for key,val in count.items():
            if mx == val:
                i = len(nums) - memo.index(key)
                j = nums.index(key)
                ans = min(i-j,ans)
        return ans
        