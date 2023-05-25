class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1
        right = len(arr)-1
        for i in range(len(arr)-1):
            if (arr[i+1] - arr[i]) > 1:
                arr[i+1] -= (arr[i+1] - arr[i] -1)
        return max(arr)