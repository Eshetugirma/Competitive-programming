class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        preSum = [0]
        for i in range(len(nums)):
            preSum.append(preSum[-1]+nums[i]%k)
        
        hashmap = defaultdict(int)
        # print(preSum)
        for i in range(len(preSum)):
            curr = preSum[i]%k
            # print(hashmap)
            if curr in hashmap and (i - hashmap[curr]) > 1:
                # print(curr,i)
                return True
            if curr not in hashmap:
                hashmap[curr] = i
        return False