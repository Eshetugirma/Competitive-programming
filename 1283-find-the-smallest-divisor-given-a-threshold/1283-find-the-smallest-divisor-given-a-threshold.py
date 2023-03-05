class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)
        #==>> use binary search to reduce time complexity
        while right > left:
            mid = (right+left)//2
            summ = 0
            #==>> find sum for every assumed to be minimum divisor
            for num in nums:
                summ += num//mid + int(num%mid != 0) 
            #==>> if sum is less than threshold then move right to mid
            if summ <= threshold:
                right = mid
            else:
                left = mid + 1
        return right