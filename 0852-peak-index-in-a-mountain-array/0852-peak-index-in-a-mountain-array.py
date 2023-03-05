class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        mx = max(arr)
        return arr.index(mx)