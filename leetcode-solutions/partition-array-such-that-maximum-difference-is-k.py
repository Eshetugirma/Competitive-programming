class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 1
        curr_min = nums[0]
        for i in range(len(nums)-1):
            if nums[i+1] - curr_min > k:
                count += 1
                curr_min = nums[i+1]
        return count


        