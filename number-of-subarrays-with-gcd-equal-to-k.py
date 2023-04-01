class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            temp = []
            right = i
            check = True
            while right < len(nums) and not nums[right]%k :
                if nums[i] == k and check:
                    check = False
                    count += 1
                temp.append(nums[right])                
                if len(temp)>=2:
                    count += int(math.gcd(*temp) == k)
                right += 1
        return count