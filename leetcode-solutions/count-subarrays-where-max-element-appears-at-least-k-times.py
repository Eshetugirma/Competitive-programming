class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        totalSubarray = 0
        n = len(nums)
        left = 0
        count = 0
        max_num = max(nums)
        for i in range(n):
            if nums[i] == max_num :
                totalSubarray += 1
            while totalSubarray >= k:
                count += n-i
                if nums[left] == max_num:
                    totalSubarray -= 1
                left += 1
        return count

            

