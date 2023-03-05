class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0
        right = len(arr)
        #==>>> binary search on index where the max up to lenght of arr
        while right > left:
            mid = (left+right)//2
            if arr[mid] > arr[mid+1] and arr[mid] > arr[mid-1]:
                return mid
            if arr[mid] < arr[mid-1]:
                right = mid 
            else:
                left = mid + 1
        return mid