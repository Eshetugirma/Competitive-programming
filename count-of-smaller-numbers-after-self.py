from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        nums.reverse()
        ans = []
        holder = SortedList()
        for num in nums:
            ans.append(holder.bisect_left(num))
            holder.add(num)
        ans.reverse()
        return ans