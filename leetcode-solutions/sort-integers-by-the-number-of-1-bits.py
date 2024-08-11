class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:

        for i in range(len(arr)):
            bits = bin(arr[i]).count('1')
            arr[i] = [bits,arr[i]]
        arr.sort()
        for i in range(len(arr)):
            arr[i] = arr[i][1]
        return  arr
        