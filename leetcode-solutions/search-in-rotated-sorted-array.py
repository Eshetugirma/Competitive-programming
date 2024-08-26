class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return -1 if target not in nums else nums.index(target)