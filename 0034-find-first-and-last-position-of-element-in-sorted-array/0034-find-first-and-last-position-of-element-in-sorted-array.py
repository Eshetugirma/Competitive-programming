class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        #===>>> this is direct use of binary search with help of bisect left and right
        starting = bisect_left(nums,target)
        ending = bisect_right(nums,target)
        if starting == ending:
            return [-1,-1]
        return [starting,ending-1]
