class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        seen = set([nums[0]])
        prefix_sum = [0]*n

        for i in range(1,n):
            prefix_sum[i] = prefix_sum[i-1] + 1
            if nums[i] not in seen:
                prefix_sum[i] -= 1
                seen.add(nums[i])

            # print(prefix_sum)
        prefix_sum.append(prefix_sum[-1])
                
        ans = float('inf')
        for left in range(n):

            right = bisect_right(nums,nums[left]+n-1)
            repititive = prefix_sum[right] - prefix_sum[left]
            window = right - left
            ans = min(ans,(n - window + repititive))
            # print(left,right,window,repititive,nums)

        return ans