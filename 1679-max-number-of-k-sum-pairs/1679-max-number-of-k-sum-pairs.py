class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        left = 0
        right = len(nums)-1
        while left < right:
            print(left,right)
            #===>>> check if sum is greater than k move right pointer
            if nums[left]+nums[right] > k:
                right -= 1
            #===>>>>> if sum is less than k then move left pointer 
            elif nums[left]+nums[right] < k:
                left += 1
            #===>>>> if i get my target point then move both pointer 
            else:
                count += 1
                right -= 1
                left += 1
        return count