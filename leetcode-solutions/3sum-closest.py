class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        prev = 10**5
        for i in range(len(nums)):
            left, right = 0, len(nums)-1
            while left < right:
                if i == left:
                    left += 1
                elif i == right:
                    right -= 1

                else:
                    curr = nums[i]+nums[left]+nums[right]
                    if abs(prev-target) > abs(curr-target):
                        prev = curr
                    if curr > target:
                        right -= 1
                    elif curr < target:
                        left += 1
                    else:
                        return target
        return prev
                        

        