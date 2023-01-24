#User function Template for python3

class Solution:
    def arraySortedOrNot(self, arr, n):
        # code here
        i = 0
        while i < n-1:
            if arr[i]>arr[i+1]:
                return 0
            i +=1
        return 1
