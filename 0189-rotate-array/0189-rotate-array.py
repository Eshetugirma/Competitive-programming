class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #===>>>>> insert the last element at zero index k times
        for i in range(k%len(nums)):
            nums.insert(0,nums.pop())
        