class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        ans = [0]*len(nums)
        print(count[0])
        if count[0] > 1:
            return ans
        elif count[0] == 1:
            current = 1
            for i in range(len(nums)):
                
                if nums[i]:
                    current *= nums[i]
                else:
                    index = i
            ans[index] = current
            return ans
        else:
            current = 1
            for i in range(len(nums)):
                current *= nums[i]
            for i in range(len(nums)):
                ans[i] = current//nums[i]
            return ans
           