class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # frequency table to store the frequency of the remainder
        remainderFrq = defaultdict(int)
        # Empty sub array will have a sum of 0 and remainder of 0, thus the frequency of 0 is 1 before we go into the array
        remainderFrq[0] = 1
        
        ans = prefixSum = 0
        for n in nums:
            # Adding n to the prefixSum, so we have the prefixSum up to the ith position.
            prefixSum += n
            # Get the remainder of the current prefixSum.
            remainder = prefixSum % k
            # We need to increase the result before update the frequency table.
            # Because we are counting how many previous prefixSum have the same remainder.
            ans += remainderFrq[remainder]
            # Update the frequency table.
            remainderFrq[remainder] += 1
        return ans




               # >> this is the brute force code for this solution ehich is my code but the above code is not mine i get it from the best solution on this problem then i used  it to modify my level
'''
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count_ans = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                if sum(nums[i:j])%k == 0:
                    count_ans += 1
        return count_ans  '''