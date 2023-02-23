class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window = (sum(nums[:k]))
        maxx = window/k
        #===>>>> by removing first value and adding next val at every window find max average
        for i in range(len(nums)-k):
            window = window - nums[i] + nums[k+i]
            maxx = max(maxx,window/k)
        return maxx