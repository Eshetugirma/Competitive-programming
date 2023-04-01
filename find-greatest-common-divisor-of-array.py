class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mx,mn = max(nums),min(nums)
        for i in range(mn,0,-1):
            if not mn%i and not mx%i:
                return i