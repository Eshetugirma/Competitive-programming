class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        seen = set()
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                left, right = j+1, len(nums)-1
                while left < right:
                    a,b,c,d = nums[i],nums[j],nums[left],nums[right]
                    if a+b+c+d == target and (a,b,c,d) not in seen:
                        ans.append([a,b,c,d])
                        seen.add((a,b,c,d))
                    elif a+b+c+d < target:
                        left += 1
                    else:
                        right -= 1
        return ans
        