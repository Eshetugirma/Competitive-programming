class Solution:
    def tribonacci(self, n: int) -> int:
        arr = [0,1,1]
        for i in range(n-2):
            arr.append(arr[i]+arr[i+1]+arr[i+2])
        return arr[n]
        