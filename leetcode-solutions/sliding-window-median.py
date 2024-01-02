from sortedcontainers import SortedList
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        window = SortedList()
        ans = []
        for i in range(k):
            window.add(nums[i])
        for i in range(len(nums)-k+1):
            if k%2:
                ans.append(window[k//2])
            else:
                ans.append((window[k//2]+window[k//2-1])/2)
            if i == (len(nums)-k):
                break
            window.remove(nums[i])
            window.add(nums[k+i])
        return ans

        