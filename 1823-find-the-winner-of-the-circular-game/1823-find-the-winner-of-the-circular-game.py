class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [i for i in range(1,n+1)]
        start = 0
        while len(arr)>1:
            start = (start+k-1)%len(arr)
            del arr[start]
        return arr[0]